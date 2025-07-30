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
    
    def make_sound(self):
        pass

class lion(Animal):
    def __init__(self , name:str , weight:float , age:int , taile_size:float ):
        super().__init__(name, weight, age)
        self._taile_size = taile_size
    
    @property
    def taile_size(self):
        return f"The size of the {self.name} tail is {self._taile_size} cm"

    @taile_size.setter
    def taile_size(self , new_size):
        if new_size < 0 :
            raise Exception("tail size cannot be negative")
        self._taile_size = new_size
    
    def make_sound(self):
        return "Roar"
    
    def info(self):
        super().info()
        print(f"The size of the {self.name} tail is {self._taile_size} cm")

class rat(Animal):
    def __init__(self , name:str , weight:float , age:int , color:str ):
        super().__init__(name, weight, age)
        self._color = color
    
    @property
    def color(self):
        return f"The color of {self.name} is {self._color} "
    
    def make_sound(self):
        return "hisses"
    
    def info(self):
        super().info()
        print(f"The color of {self.name} is {self._color} ")

class snake(Animal):
    def __init__(self , name:str , weight:float , age:int ,venomous: bool ):
        super().__init__(name, weight, age)
        self._venomous = venomous
    
    @property
    def venomous(self):
        if self._venomous == True:
            return f"{self.name} is venomous"
        else:
            return f"{self.name} is not venomous"
    
    def make_sound(self):
        return "sisss"
    
    def info(self):
        super().info()
        print(f"{self.name} is {'venomous' if self._venomous else 'not venomous'}")

