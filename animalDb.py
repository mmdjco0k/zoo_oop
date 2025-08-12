import sqlite3
import animal 
import pickle
import json
class AnimalStorage:
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
    def save_to_db(self , animals):
        self.cursor.execute('''DELETE FROM animals''')

        for animal in animals:
           self.cursor.execute('INSERT INTO animals (animal) VALUES (?)', (pickle.dumps(animal),))
        self.conn.commit()
    
    def get_animals(self):
        self.cursor.execute('SELECT animal FROM animals')
        animals = self.cursor.fetchall()
        for animal in animals:
            animal_data = pickle.loads(animal[0])
            self.animal_list.append(animal_data)
        return self.animal_list

    def save_to_json(self):
        with open("animals.json", 'w', encoding='utf-8') as file:
            json.dump([animal.to_json() for animal in self.animal_list], file)
