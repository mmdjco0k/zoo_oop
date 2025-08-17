from permission import custom_permission
import permission as p
from zoo import Zoo
import ExceptionHandeling as eh
from CustomLogger import CustomLogger
from animalDb import AnimalStorage
from animals.animal import Animal
from authorization import login
from animals.serializers import AnimalSerializer
import json


zoo = Zoo()
animal_logger = CustomLogger('animal.log')

storage_type = input('Enter storage tyoe (csv , json ,sqlite): ')

storage = AnimalStorage.create_with_strategy(storage=storage_type)

zoo.animals_list=storage.load()

serilizer = AnimalSerializer()



def print_info(animal):
    print(f"\nname is {animal["name"]}")
    print(f"id is {animal["id"]}")
    print(f"age is {animal["age"]}")
    print(f"weight is {animal["weight"]}")

    animal_type = animal["animal_type"]
    match animal_type:
        case "lion":
            print(f"The size of the {animal["name"]} tail is {animal["tail_size"]} cm")
            print(f"The strength of the {animal["name"]} is {animal['strength']}")
            print(f"The {animal["name"]} {'is the' if animal["herd_leader"] else 'is not the'} herd leader")
        case "rat":
            print(f"The color of {animal["name"]} is {animal['color']} ")
            print(f"The {animal["name"]} {'can' if animal['climbing'] else 'can not'} climb")
            print(f"The {animal["name"]} {'can' if animal['digging'] else 'can not'} digging")
        case "snake":
            print(f"{animal["name"]} is {'venomous' if animal["venomous"] else 'not venomous'}")
            print(f"{animal["name"]} is {'tamed' if animal["tamed"] else 'not tamed'}")
            print(f'{animal["name"]} length is {animal["length"]}')

def print_menu():    
    print('\n1 : add animal')
    print('2 : delete animal')
    print('3 : show all animal')
    print('4 : search by the name')
    print('5 : search by the id')
    print('6 : counting the number of animals of each species')
    print('7 : get log')
    print('8 : login')
    operation = int(input("\nenter a number : "))
    return operation

def add_animal(animal_type, role):
    animal_properties = {
        "lion": ["name", "weight", "age", "tail_size", "herd_leader", "strength"],

        "rat": ["name", "weight", "age", "color", "climbing_ability", "digging_ability"],

        "snake": ["name", "weight", "age", "venomous", "tamed", "length"]
    }
    
    property_types = {
        "lion": {"weight": float, "age": int, "tail_size": float, "herd_leader": bool, "strength": int},

        "rat": {"weight": float, "age": int, "climbing_ability": bool,"digging_ability": bool},

        "snake": {"weight": float, "age": int, "venomous": bool,"tamed": bool, "length": float}
    }
    
    try:
        if animal_type not in animal_properties:
            print('\nInvalid input!')
            operations(role=role)
            return
            
        properties = {}
        for prop in animal_properties[animal_type]:
            input_prop = input(f"Enter {prop}:")
            
            if prop in property_types[animal_type]:
                prop_type = property_types[animal_type][prop]
                input_prop = prop_type(input_prop)
                
            properties[prop] = input_prop
        
        if zoo.create(role=role ,animal_type=animal_type, **properties):
            storage.save(zoo.animals_list)
            print(f"\nThe {animal_type} info:")
            print_info(serilizer.to_json(zoo.search_by_name(role , name=properties['name'])))
            
    except Exception as e:
        animal_logger.error(f"validation error :{e}")
        print("\nYou gave the wrong input!")

def operations(role):
    while True:
        operation = print_menu()
        match operation:
            case 1:
                animal_type = input("\nEnter animal type (lion , rat , snake):")
                add_animal(animal_type=animal_type , role=role)
            case 2:
                    animal_name = input("\nEnter animal name:")
                    animal = zoo.search_by_name(role , animal_name)
                    if isinstance(animal , Animal):
                        input_qu = input("\nare you sure you want to destroy this animal ( y / n ) :")
                        if input_qu == 'y':
                            if zoo.destroy(role=role , animal=animal):
                                print('the animal is deleted')
                                storage.save(zoo.animals_list)
                        elif input_qu == 'n':
                            print('ok')
                        else :
                            print('\ninvalid input!')
            case 3:
                zoo.ShowList(role=role)
            case 4:
                name = input('Enter the name of animal:')
                animal = zoo.search_by_name(role , name=name)
                if animal == None:
                    print('\nthis animal is not exist!')
                else:
                    print_info(serilizer.to_json(animal))
            case 5:
                id = input('Enter the id of animal:')
                animal = zoo.search_by_id(role , id=id)
                if animal == None:
                    print('\nthis animal is not exist!')
                else:
                    print_info(serilizer.to_json(animal))
            case 6:
                zoo.counter()
            case 7:
                with open('animal.log', 'r', encoding='utf-8') as file:
                    print(file.read())            
            case 8:
                try:
                    if not custom_permission.logged_in(role=role):
                        role = login()
                except p.PermissionError as e:
                        print(e.args[0])
            case _:
                print("\ninvalid input!")




operations('user')
