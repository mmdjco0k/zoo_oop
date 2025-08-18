from animals.lion import Lion
from animals.snake import Snake
from animals.rat import Rat
from permission import custom_permission
from CustomLogger import CustomLogger
import permission as p
import ExceptionHandeling as eh
import sqlite3
import json
import pickle
from animals.serializers import AnimalSerializer 
animal_logger = CustomLogger('animal.log')


class Zoo:
    def __init__(self ):
        self.animals_list = []
        self.permission = custom_permission()
    
    def check_permission(self , role , method_name):
        try:
            return self.permission.has_permission(role=role, method_name=method_name)
        except p.PermissionError as e:
            animal_logger.error(f"a user tried to {method_name} and could not:{e}")
            print(e.args[0])

    def create_animal(self, animal_type, name, weight, age, **kwargs):
        animal_classes = {
            "lion": Lion,
            "snake": Snake,
            "rat": Rat
        }
        
        if animal_type not in animal_classes:
            eh.raise_error(7)
            
        return animal_classes[animal_type](
            animal_type=animal_type,
            name=name,
            weight=weight,
            age=age,
            **kwargs
        )

    def validation(self , name):
        for i in self.animals_list:
            if i.name == name :
                eh.raise_error(9)
    def create(self , role , animal_type , name , weight , age , **kwargs):
        if self.check_permission(role, 'create'):
            try:
                self.validation(name)
                animal = self.create_animal(animal_type , name , weight , age , **kwargs)
                self.animals_list.append(animal)
                return True
            except eh.InvalidInput as e:
                print("\n",e.args[0])
                return False            


    def destroy(self , role , animal):
        if self.check_permission(role, 'destroy'):
            self.animals_list.remove(animal)
            del animal
            return True
        return False
        
    def ShowList(self , role):
        if self.check_permission(role, 'show_list'):
            if len(self.animals_list) != 0:
                for AnimalObject in self.animals_list:
                    print("\n")
                    from cli import print_info
                    print_info(AnimalSerializer().to_json(AnimalObject))
            else :
                print("\nThere is no animal in the zoo")

    def search_by_id(self , role , id ):
        if self.check_permission(role, 'search_by_id'):
            for AnimalObject in self.animals_list:
                if AnimalObject.id == int(id):
                    return AnimalObject
            print('\ninvalid input!')
            return None

    def search_by_name(self , role ,name):
        if self.check_permission(role, 'search_by_name'):
            for AnimalObject in self.animals_list:
                if AnimalObject.name == name :
                    return AnimalObject
            print('\ninvalid input!')
            return None
 
    def counter(self):
        lion_counter = 0
        rat_counter = 0
        snake_counter = 0
        for AnimalObject in self.animals_list:
            if AnimalObject.animal_type == "lion":
                lion_counter += 1
            elif AnimalObject.animal_type == "rat":
                rat_counter += 1
            elif AnimalObject.animal_type == "snake":
                snake_counter += 1
        print(f"We have {lion_counter} of lions")
        print(f"We have {rat_counter} of rats")
        print(f"We have {snake_counter} of snakes")

