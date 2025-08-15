import permission as p
from zoo import Zoo
import ExceptionHandeling as eh
from CustomLogger import CustomLogger
from animalDb import AnimalStorage
import json

admin_username = "admin"
admin_password = "admin123"

zoo = Zoo()
animal_logger = CustomLogger('animal.log')

storage = AnimalStorage.create_with_strategy(storage="csv")
zoo.animals_list=storage.load()

def print_menu(status):    
    match status:
        case "start":
            print('\n1 : login as admin')
            print('2 : enter as user (no login requierd)')
            user_input = int(input("\nEnter a number : "))
            return user_input

        case "operations":
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
            print("prop is :" , prop)
            input_prop = input(f"Enter {prop}:")
            
            if prop in property_types[animal_type]:
                prop_type = property_types[animal_type][prop]
                print(prop_type)
                input_prop = prop_type(input_prop)
                
            properties[prop] = input_prop
        
        if zoo.create(animal_type=animal_type, **properties):
            storage.save(zoo.animals_list)
            print(f"\nThe {animal_type} info:")
            zoo.search_by_name(name=properties['name'])
            
    except Exception as e:
        animal_logger.error(f"validation error :{e}")
        print("\nYou gave the wrong input!")



def operations(role):
    while True:
        operation = print_menu('operations')
        match operation:
            case 1:
                try:
                    if permission(role=role):
                        animal_type = input("\nEnter animal type (lion , rat , snake):")
                        add_animal(animal_type=animal_type , role=role)
                except p.PermissionError as e:
                        animal_logger.error(f"a user try to create a new animal:{e}")
                        print(e.args[0])
            case 2:
                try:
                    if permission(role=role):
                        animal_name = input("\nEnter animal name:")
                        zoo.destroy(name=animal_name)
                        animal_logger.info(f'{animal_name} is deleted from list')
                except p.PermissionError as e:
                        animal_logger.error(f"a user try to delete an animal:{e}")
                        print(e.args[0])
            case 3:
                zoo.ShowList()
            case 4:
                name = input('Enter the name of animal:')
                zoo.search_by_name(name=name)
            case 5:
                id = input('Enter the id of animal:')
                zoo.search_by_id(id=id)
            case 6:
                zoo.counter()
            case 7:
                with open('animal.log', 'r', encoding='utf-8') as file:
                    print(file.read())            
            case 8:
                try:
                    if logged_in(role):
                        login()
                except p.PermissionError as e:
                        print(e.args[0])
            case _:
                print("\ninvalid input!")


def login():
    while True:
        user_input = print_menu('start')
        match user_input:
            case 1:
                username = input("\nenter username : ")
                password = input("enter password : ")
                if (username == admin_username and password == admin_password) :
                    role = 'admin'
                    animal_logger.info("admin logged in")
                    operations(role=role)
                else :
                    animal_logger.warning("somone tried to login!")
                    print("\nusername or password is wrong!")

            case 2:
                operations(role=role)
                break
            case _:
                print('\nyour input is invalid!s')

def permission(role):
    if role == "admin":
        return True
    p.raise_permission_error(1)

def logged_in(role):
    if role == "admin":
        p.raise_permission_error(2)
    return True

operations('user')