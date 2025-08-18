from abc import ABC , abstractmethod
import ExceptionHandeling as eh
from CustomLogger import CustomLogger

animal_logger = CustomLogger('animal.log')

class Animal(ABC):
    counter = 0
    def __init__(self , name:str , weight:float , age:int ):
        self.name = name 
        self._age = age
        self._weight = weight
        self._id = Animal.counter
        self._animal_type = None
        Animal.counter += 1
        

    def validation(self , name , weight , age):
        if not None and not isinstance(weight ,float) :
            animal_logger.error(f"validation error weight error{weight}")
            eh.raise_error(15)
        elif weight <= 0:
            eh.raise_error(1)
            animal_logger.error(f"validation error weight error")

        if not None and not isinstance(age , int) :
            eh.raise_error(16)
            animal_logger.error(f"validation error age error")

        elif age<0:
            animal_logger.error(f"validation error age error")
            eh.raise_error(2)
        if not None and not isinstance(name , str):
            animal_logger.error(f"validation error name error")
            eh.raise_error(17)

    @property
    def id(self):
        return self._id

    
    @property
    def weight(self):
        return self._weight
    
    @property
    def age(self):
        return self._age
    
    @property
    def animal_type(self):
        return self._animal_type

    @animal_type.setter
    def animal_type(self , value):
            eh.raise_error(8)


    @id.setter
    def id(self , value):
            eh.raise_error(3)
 
    @age.setter
    def age(self , new_age ):
        if new_age < self._age or new_age < 0:
            eh.raise_error(4)
        self._age = new_age

    @weight.setter
    def weight(self , new_weight):
        if new_weight <= 0:
            eh.raise_error(1)
        self._weight = new_weight
    
    def eat(self):
        return f"The {self.name} is eating"
    
    def sleep(self):
        return f"The {self.name} is sleeping"
    

    def make_sound(self):
        pass

    def __str__(self):
        return f"{self.name} ({self._animal_type}) - Age: {self.age}, Weight: {self.weight}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name='{self.name}', weight={self.weight}, age={self.age})"