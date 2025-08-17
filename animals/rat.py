from .animal import Animal
from CustomLogger import CustomLogger
import ExceptionHandeling as eh

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

