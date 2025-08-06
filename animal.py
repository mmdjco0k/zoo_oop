from abc import ABC , abstractmethod
import ExceptionHandeling as eh
from CustomLogger import CustomLogger

animal_logger = CustomLogger('animal.log')

class Animal(ABC):
    counter = 0
    def __init__(self , name:str , weight:float , age:int ):
        animal_logger.info(f"create new animal name is {name}")
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
    
    
    def info(self):
        print(f"\nname is {self.name}")
        print(f"id is {self._id}")
        print(f"age is {self._age}")
        print(f"weight is {self._weight}")
    
    def make_sound(self):
        pass

class lion(Animal):
    def __init__(self , animal_type:str , name:str , weight:float , age:int , taile_size:float , herd_leader:bool  , strength:int  ):
        self.validation(name=name , weight=weight , age=age , taile_size=taile_size , herd_leader=herd_leader , strength=strength)
        super().__init__(name, weight, age)
        self._animal_type = animal_type
        self._taile_size = taile_size
        self._herd_leader = herd_leader
        self._strength = strength
    

    def validation(self, name , weight, age, taile_size , herd_leader , strength):
        super().validation(name=name , weight=weight , age=age)
 
        if taile_size < 0 :
            animal_logger.error(f"validation error")

            eh.raise_error(6)
        elif not None and not isinstance(taile_size , float):
            animal_logger.error(f"validation error")
            eh.raise_error(15)
        
        if  not None and not isinstance(herd_leader, bool):
            animal_logger.error(f"validation error")
            eh.raise_error(11)
        
        if not 1 <= strength <= 10:
            animal_logger.error(f"validation error")
            eh.raise_error(10)
        elif not None and not isinstance(strength , int):
            animal_logger.error(f"validation error")
            eh.raise_error(16)
        
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
            if not isinstance(new_value , bool):
                eh.raise_error(11)
            self.herd_leader == new_value
    
    def make_sound(self):
        return "Roar"
    
    def info(self):
        super().info()
        print(f"The size of the {self.name} tail is {self._taile_size} cm")
        print(f"The strength of the {self.name} is {self._strength}")
        print(f"The {self.name} {'is the' if self._herd_leader else 'is not the'} herd leader")




class rat(Animal):
    def __init__(self , animal_type:str , name:str , weight:float , age:int , color:str , climbing_ability:bool , digging_ability:bool):
        self.validation(name=name , weight=weight , age=age , climbing_ability=climbing_ability , digging_ability=digging_ability)
        super().__init__(name, weight, age)
        self._animal_type = 'rat'
        self._color = color
        self._climbing_ability = climbing_ability
        self._digging_ability = digging_ability

    def validation(self , name , weight , age , climbing_ability , digging_ability):
        super().validation(name=name , weight=weight , age=age)
        
        if not None and not isinstance(climbing_ability , bool):
            animal_logger.error(f"validation error")
            eh.raise_error(11)
        if not None and not isinstance(digging_ability , bool):
            animal_logger.error(f"validation error")
            eh.raise_error(11)

    @property
    def climbing_ability(self):
        if self._climbing_ability == True:
            print(f"The {self.name} can climb")
        else :
            print(f"The {self.name} can not climb")
    
    @climbing_ability.setter
    def climbing_ability(self , new_value):
        if not None and not isinstance(new_value , bool):
            eh.raise_error(11)
        self._climbing_ability = new_value

    @property
    def digging_ability(self):
        if self._digging_ability == True:
            print(f"The {self.name} can digging")
        else :
            print(f"The {self.name} can not digging")
    
    @digging_ability.setter
    def digging_ability(self , new_value ) :
        if not None and not isinstance(new_value , bool):
            eh.raise_error(11)
        self._digging_ability = new_value

    @property
    def color(self):
        return f"The color of {self.name} is {self._color}"
    
    def make_sound(self):
        return "hisses"
    
    def info(self):
        super().info()
        print(f"The color of {self.name} is {self._color} ")
        print(f"The {self.name} {'can' if self._climbing_ability else 'can not'} climb")
        print(f"The {self.name} {'can' if self._digging_ability else 'can not'} digging")




class snake(Animal):
    def __init__(self , animal_type:str , name:str , weight:float , age:int ,venomous: bool , tamed : bool , length:float ):
        self.validation(name=name , weight=weight , age=age , venomous=venomous , tamed=tamed , length=length)
        super().__init__(name, weight, age)
        self._animal_type = 'snake'
        self._venomous = venomous
        self._tamed = tamed
        self._length = length

    def validation(self ,name ,weight , age , venomous , tamed , length):
        super().validation(name=name , weight=weight , age=age)
        if not None and not isinstance(venomous , bool):
            animal_logger.error(f"validation error")
            eh.raise_error(11)
        if not None and not isinstance(tamed , bool):
            animal_logger.error(f"validation error")
            eh.raise_error(11)
        if length is None or not isinstance(length, float):
            animal_logger.error(f"validation error")
            eh.raise_error(15)

    @property
    def venomous(self):
        if self._venomous == True:
            return f"{self.name} is venomous"
        else:
            return f"{self.name} is not venomous"
    
    @venomous.setter
    def venomous(self , new_value):
        if not None and not isinstance(new_value , bool):
            eh.raise_error(11)
        self._venomous = new_value

    @property
    def tamed(self):
        if self._tamed == True:
            return f"{self.name} is tamed"
        else:
            return f"{self.name} is not tamed"
    
    @tamed.setter
    def tamed(self , new_value):
        if not None and not isinstance(new_value , bool):
            eh.raise_error(11)
        self._tamed = new_value
    
    @property
    def length(self):
        print(f'{self.name} length is {self._length}')
    
    @length.setter
    def length(self , new_value):
        if new_value is None or not isinstance(new_value, float):
            eh.raise_error(15)
        self._length = new_value

    def make_sound(self):
        return "sisss"
    
    def info(self):
        super().info()
        print(f"{self.name} is {'venomous' if self._venomous else 'not venomous'}")
        print(f"{self.name} is {'tamed' if self._tamed else 'not tamed'}")
        print(f'{self.name} length is {self._length}')
