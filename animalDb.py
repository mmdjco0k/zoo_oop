import sqlite3
from animals.animal import Animal
import pickle
import json
import csv
from abc import ABC , abstractmethod
class Storage(ABC):
    @abstractmethod
    def save(self , animals):
        pass

    @abstractmethod
    def load(self):
        pass

class SqliteStorage(Storage):
    def __init__(self , DbName = 'a.db'):
        self.conn = sqlite3.connect(DbName)
        self.cursor = self.conn.cursor()
        self.tables = self.tables()
        self.animal_list = []
    def tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS animals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                animal TEXT
            )
        ''')
        self.conn.commit()
    def save(self , animals):
        self.cursor.execute('''DELETE FROM animals''')
        for animal in animals:
            self.cursor.execute('INSERT INTO animals (animal) VALUES (?)',
                              (pickle.dumps(animal),))
        self.conn.commit()
    
    def load(self):
        self.cursor.execute('SELECT animal FROM animals')
        animals = self.cursor.fetchall()
        animal_list = []
        for animal in animals:
            animal_data = pickle.loads(animal[0])
            animal_list.append(animal_data)
        return animal_list

class JsonStorage(Storage):
    def __init__(self, file_name='animals.json'):
        self.file_name = file_name
    
    def save(self, animals):
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump([animal.to_json() for animal in animals], file)
    
    def load(self):
        with open(self.file_name, 'r', encoding='utf-8') as file:
            animals_data = json.load(file)
        return [Animal.from_json(data) for data in animals_data]

class CsvStorage(Storage):
    def __init__(self, file_name='animals.csv'):
        self.file_name = file_name

    def save(self, animals):
        fields = set()

        for animal in animals:
            fields.update(animal.to_json().keys())
        
        fieldnames = list(fields)
        
        with open(self.file_name, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for animal in animals:
                writer.writerow(animal.to_json())

    def load(self):
        with open(self.file_name, 'r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            animals_data = list(reader)
        return [Animal.from_csv(data) for data in animals_data]


class AnimalStorage:    
    def __init__(self, storage=None):
        self.storage = storage
        self.animal_list = []

    @classmethod
    def create_with_strategy(cls, storage):
        strategies = {
            'sqlite' : SqliteStorage(),
            'json' : JsonStorage(),
            'csv' : CsvStorage()
        }
        return cls(strategies.get(storage))
    
    def save(self, animals):
        self.storage.save(animals)
    
    def load(self):
        self.animal_list = self.storage.load()
        return self.animal_list
