from .lion import Lion
from .rat import Rat
from .snake import Snake
class AnimalSerializer:
    @staticmethod
    def json_base(animal_object):
        dictionary = {"animal_type":animal_object.animal_type ,"name":animal_object.name
            , "id":animal_object._id  , "age":animal_object._age , "weight":animal_object._weight}
        return dictionary
    
    @staticmethod
    def to_json(data):
        animal_type = data.animal_type
        match animal_type:
            case "lion":
                return LionSerializer.to_json(data)
            case "rat":
                return RatSerilizer.to_json(data)
            case "snake":
                return SnakeSerializer.to_json(data)
            case _:
                eh.raise_error(7)

    @staticmethod
    def from_json(data):
        animal_type = data.get('animal_type')
        match animal_type:
            case "lion":
                return LionSerializer.from_json(data)
            case "rat":
                return RatSerilizer.from_json(data)
            case "snake":
                return SnakeSerializer.from_json(data)
            case _:
                eh.raise_error(7)
    
    @staticmethod
    def from_csv(data):
        animal_type = data.get("animal_type")
        match animal_type:
            case "lion":
                return LionSerializer.from_csv(data)
            case "rat":
                return RatSerilizer.from_csv(data)
            case "snake":
                return SnakeSerializer.from_csv(data)
            case _:
                eh.raise_error(7)


class LionSerializer:
    @staticmethod
    def to_json(animal_object):
        base = AnimalSerializer.json_base(animal_object=animal_object)
        lion_properties = {"tail_size":animal_object._tail_size , "herd_leader":animal_object._herd_leader , "strength":animal_object._strength}
        base.update(lion_properties)
        return base

    @staticmethod
    def from_json(data):
        return Lion(
            animal_type=data['animal_type'],
            name=data['name'],
            weight=data['weight'],
            age=data['age'],
            tail_size=data['tail_size'],
            herd_leader=data['herd_leader'],
            strength=data['strength']
        )
    @staticmethod
    def from_csv(data):
        return Lion(
            animal_type=data['animal_type'],
            name=data['name'],
            weight=float(data['weight']),
            age=int(data['age']),
            tail_size=float(data['tail_size']),
            herd_leader=bool(data['herd_leader']),
            strength=int(data['strength'])
        )

class RatSerilizer:
    @staticmethod
    def to_json(animal_object):
        base = AnimalSerializer.json_base(animal_object=animal_object)
        rat_properties = {"color":animal_object._color , "climbing":animal_object._climbing_ability , "digging":animal_object._digging_ability}    
        base.update(rat_properties)
        return base
    
    @staticmethod
    def from_json(data):
        return Rat(
            animal_type=data['animal_type'],
            name=data['name'],
            weight=data['weight'],
            age=data['age'],
            color=data['color'],
            climbing_ability=data['climbing'],
            digging_ability=data['digging']
        )
    
    @staticmethod
    def from_csv(data):
        return Rat(
            animal_type=data['animal_type'],
            name=data['name'],
            weight=float(data['weight']),
            age=int(data['age']),
            color=data['color'],
            climbing_ability=bool(data['climbing']),
            digging_ability=bool(data['digging'])
        )

class SnakeSerializer:
    @staticmethod
    def to_json(animal_object):
        base = AnimalSerializer.json_base(animal_object=animal_object)
        snake_properties = {"venomous":animal_object._venomous , "tamed":animal_object._tamed , "length":animal_object._length}
        base.update(snake_properties)
        return base
    
    @staticmethod
    def from_json(data):
        return Snake(
            animal_type=data['animal_type'],
            name=data['name'],
            weight=data['weight'],
            age=data['age'],
            venomous=data['venomous'],
            tamed=data['tamed'],
            length=data['length']
        )
    @staticmethod
    def from_csv(data):
        return Snake(
            animal_type=data['animal_type'],
            name=data['name'],
            weight=float(data['weight']),
            age=int(data['age']),
            venomous=bool(data['venomous']),
            tamed=bool(data['tamed']),
            length=float(data['length'])
        )