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
    
    
    def to_json(self):
        dictionary = {"animal_type":self.animal_type ,"name":self.name , "id":self._id  , "age":self._age , "weight":self._weight}
        return dictionary


    def make_sound(self):
        pass

    @classmethod
    def from_json(cls , data):
        animal_type = data.get('animal_type')
        match animal_type:
            case "lion":
                from .lion import Lion  

                return Lion.from_json(data)
            case "rat":
                from .rat import Rat


                return Rat.from_json(data)
            case "snake":
                from .snake import Snake

                return Snake.from_json(data)
            case _:
                eh.raise_error(7)
    
    @classmethod
    def from_csv(clas , data):
        animal_type = data.get("animal_type")
        match animal_type:
            case "lion":
                from .lion import Lion  

                return Lion.from_csv(data)
            case "rat":
                from .rat import Rat
                return Rat.from_csv(data)
            case "snake":
                from .snake import Snake
                return Snake.from_csv(data)
            case _:
                eh.raise_error(7)





