from .animal import Animal
from CustomLogger import CustomLogger

animal_logger = CustomLogger('animal.log')

class Rat(Animal):
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
   
    def to_json(self):
        base = super().to_json()
        rat_properties = {"color":self._color , "climbing":self._climbing_ability , "digging":self._digging_ability}    
        base.update(rat_properties)
        return base

    @classmethod
    def from_json(cls, data):
        return cls(
            animal_type=data['animal_type'],
            name=data['name'],
            weight=data['weight'],
            age=data['age'],
            color=data['color'],
            climbing_ability=data['climbing'],
            digging_ability=data['digging']
        )

    @classmethod
    def from_csv(cls , data):
        return cls(
            animal_type=data['animal_type'],
            name=data['name'],
            weight=float(data['weight']),
            age=int(data['age']),
            color=data['color'],
            climbing_ability=bool(data['climbing']),
            digging_ability=bool(data['digging'])
        )