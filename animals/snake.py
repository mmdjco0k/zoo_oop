from .animal import Animal
from CustomLogger import CustomLogger
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
    
    def info(self):
        super().info()
        print(f"{self.name} is {'venomous' if self._venomous else 'not venomous'}")
        print(f"{self.name} is {'tamed' if self._tamed else 'not tamed'}")
        print(f'{self.name} length is {self._length}')

    def to_json(self):
        base = super().to_json()
        snake_properties = {"venomous":self._venomous , "tamed":self._tamed , "length":self._length}

        base.update(snake_properties)
        return base
    
    @classmethod
    def from_json(cls, data):
        return cls(
            animal_type=data['animal_type'],
            name=data['name'],
            weight=data['weight'],
            age=data['age'],
            venomous=data['venomous'],
            tamed=data['tamed'],
            length=data['length']
        )
    
    @classmethod
    def from_csv(cls , data):
        return cls(
            animal_type=data['animal_type'],
            name=data['name'],
            weight=float(data['weight']),
            age=int(data['age']),
            venomous=bool(data['venomous']),
            tamed=bool(data['tamed']),
            length=float(data['length'])
        )