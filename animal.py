from abc import ABC , abstractmethod
import ExceptionHandeling as eh

class Animal(ABC):
    counter = 0
    def __init__(self , name:str , weight:float , age:int ):
        # self.validationـ(weight=weight , age=age)
        self.name = name 
        self._age = age
        self._weight = weight
        self._id = Animal.counter
        self._animal_type = None
        Animal.counter += 1
        

    def validation(self , weight , age):
        if weight <= 0 :
            eh.raise_error(1)
        
        if age<0:
            eh.raise_error(2)


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
    
    
    def info(self):
        print(f"name is {self.name}")
        print(f"age is {self._age}")
        print(f"weight is {self._weight}")
    
    def make_sound(self):
        pass

class lion(Animal):
    def __init__(self , name:str , weight:float , age:int , taile_size:float , herd_leader:bool  , strength:int  ):
        self.validation(weight=weight , age=age , taile_size=taile_size , herd_leader=herd_leader , strength=strength)
        super().__init__(name, weight, age)
        self._animal_type = 'lion'
        self._taile_size = taile_size
        self._herd_leader = herd_leader
        self._strength = strength

    def validation(self, weight, age, taile_size , herd_leader , strength):
        super().validation(weight=weight , age=age)

        if taile_size < 0 :
            eh.raise_error(6)
        
        if  not isinstance(herd_leader, bool):
            eh.raise_error(11)
        
        if not 1 <= strength <= 10:
            eh.raise_error(10)
        
    @property
    def taile_size(self):
        return f"The size of the {self.name} tail is {self._taile_size} cm"

    @taile_size.setter
    def taile_size(self , new_size):
        if new_size < 0 :
            eh.raise_error(6)
        self._taile_size = new_size
    @property
    def strength(self):
            return f"The strength of the {self.name} is {self._strength}"
        
    @strength.setter
    def strength(self , new_strength):
            if not 1 <= new_strength <= 10:
                eh.raise_error(10)
            self.strength = new_strength
        
    @property
    def herd_leader(self):
            if self._herd_leader == True:
                print(f"The {self.name} is the herd leader")
            else :
                print(f"The {self.name} is not the herd leader")
        
    @herd_leader.setter
    def herd_leader(self , new_value):
            if type(herd_leader) != bool:
                eh.raise_error(11)
            self.herd_leader == new_value
    
    def make_sound(self):
        return "Roar"
    
    def info(self):
        super().info()
        print(f"The size of the {self.name} tail is {self._taile_size} cm")

class rat(Animal):
    def __init__(self , name:str , weight:float , age:int , color:str  ):
        super().__init__(name, weight, age)
        self._animal_type = 'rat'
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
        self._animal_type = 'snake'
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

