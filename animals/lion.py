from .animal import Animal
from CustomLogger import CustomLogger
import ExceptionHandeling as eh


animal_logger = CustomLogger('animal.log')

class Lion(Animal):
    def __init__(self , animal_type:str , name:str , weight:float , age:int , tail_size:float , herd_leader:bool  , strength:int  ):
        self.validation(name=name , weight=weight , age=age , tail_size=tail_size , herd_leader=herd_leader , strength=strength)
        super().__init__(name, weight, age)
        self._animal_type = animal_type
        self._tail_size = tail_size
        self._herd_leader = herd_leader
        self._strength = strength
    

    def validation(self, name , weight, age, tail_size , herd_leader , strength):
        super().validation(name=name , weight=weight , age=age)
 
        if tail_size < 0 :
            animal_logger.error(f"validation error")

            eh.raise_error(6)
        elif not None and not isinstance(tail_size , float):
            animal_logger.error(f"validation error")
            eh.raise_error(15)
        
        if  not isinstance(herd_leader, bool):
            animal_logger.error(f"validation error")
            eh.raise_error(11)
        
        if not None and not isinstance(strength , int):
            animal_logger.error(f"validation error")
            eh.raise_error(16)
        elif not 1 <= strength <= 10:
            animal_logger.error(f"validation error")
            eh.raise_error(10)

        
    @property
    def tail_size(self):
        return f"The size of the {self.name} tail is {self._tail_size} cm"

    @tail_size.setter
    def tail_size(self , new_size):
        if new_size < 0 :
            eh.raise_error(6)
        self._tail_size = new_size
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
    
    def __str__(self):
        leader_status = "herd leader" if self._herd_leader else "not herd leader"
        return super().__str__() + f"\nTail Size: {self.tail_size}, Role: {leader_status}, Strength: {self.strength}"

    def __repr__(self):
        return (f"{self.__class__.__name__}(name='{self.name}', "
                f"weight={self.weight}, age={self.age}, "
                f"tail_size={self.tail_size}, herd_leader={self._herd_leader}, strength={self.strength})")