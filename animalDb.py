import sqlite3
import animal 
import pickle
import json
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


class AnimalStorage:    
    def __init__(self, storage=None):
        self.storage = storage
        self.animal_list = []

    @classmethod
    def create_with_strategy(cls, storage):
        strategies = {
            'sqlite': SqliteStorage(),
        }
        return cls(strategies.get(storage))
    
    def save(self, animals):
        self.storage.save(animals)
    
    def load(self):
        self.animal_list = self.storage.load()
        return self.animal_list
