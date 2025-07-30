from abc import ABC , abstractmethod
import uuid


class Animal(ABC):
    def __init__(self , name:str , weight:float , age:int):
        self.validation(weight=weight , age=age)
        self.name = name 
        self._age = age
        self._weight = weight
        self._id = int(uuid.uuid4())

    def validation(self , weight , age):
        if weight <= 0 :
            raise Exception("The weight must be positive")
        
        if age<0:
            raise Exception("age cannot be negative")


    @property
    def id(self):
        return f"id is {self._id }"

    
    @property
    def weight(self):
        return f"weight is {self._weight}"
    
    @property
    def age(self):
        return f"age is {self._age }"
    
    @id.setter
    def id(self, value):
        raise Exception("you can not change id ")
    
    @age.setter
    def age(self , new_age ):
        if new_age < self._age or new_age < 0:
            raise Exception("there is a problem")    
        self._age = new_age

    @weight.setter
    def weight(self , new_weight):
        if new_weight <= 0:
            raise Exception("The weight must be positive")
        self._weight = new_weight
    
    def eat(self):
        return f"The {self.name} is eating"
    
    def sleep(self):
        return f"The {self.name} is sleeping"
    

    def info(self):
        print(f"name is {self.name}")
        print(f"age is {self._age}")
        print(f"weight is {self._weight}")

