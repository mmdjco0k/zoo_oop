from .animal import Animal
from CustomLogger import CustomLogger
import ExceptionHandeling as eh
animal_logger = CustomLogger('animal.log')

class Snake(Animal):
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
        if not None and not isinstance(length, float):
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

    def __str__(self):
        venom_status = "venomous" if self._venomous else "not venomous"
        tame_status = "tamed" if self._tamed else "wild"
        return super().__str__() + f"\nLength: {self.length}, Status: {venom_status}, {tame_status}"

    def __repr__(self):
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"weight={self.weight}, age={self.age}, "
                f"venomous={self._venomous}, tamed={self._tamed}, length={self.length})")