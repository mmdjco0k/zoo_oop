import permission as p
from zoo import Zoo
import ExceptionHandeling as eh
from CustomLogger import CustomLogger
from animalDb import AnimalDb
import json

admin_username = "admin"
admin_password = "admin123"

zoo = Zoo()
animal_logger = CustomLogger('animal.log')

db = AnimalDb()
zoo.animals_list=db.get_animals()

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
            print('8 : save data in data base')
            print('9 : login')
            print('10 : save in json')
            operation = int(input("\nenter a number : "))
            return operation

def add_animal(animal_type , role):
    match animal_type:
        case "lion":
            try:
                name = input("Enter lion name:")
                weight = input("Enter lion weight(number):")
                age = input("Enter lion age(number):")
                tail_size = input("Enter lion tail size(number):")
                herd_leader = input('Enter status herd leader of lion (True or False):')
                strength = input("Enter strength of lion (1 to 10):")
                if zoo.create(animal_type="lion" , name=name , weight=float(weight) , age=int(age) , tail_size=float(tail_size) , herd_leader=bool(herd_leader) , strength=int(strength)):
                    print("\nThe lion info:")
                    l = zoo.search_by_name(name=name)
            except Exception as e:
                animal_logger.error(f"validation error :{e}")
                print("\nYou gave the wrong input!")

        case "rat":
            try:
                name = input("Enter rat name:")
                weight = input("Enter rat weight(number):")
                age = input("Enter rat age(number):")
                color = input("Enter rat color:")
                climbing_ability = input("Cat this rat climnb? (True or False):")
                digging_ability = input("Can this rat dig? (True of False):")
                if zoo.create(animal_type="rat" , name=name , weight=float(weight) , age=int(age) , color=color , climbing_ability=bool(climbing_ability) , digging_ability=bool(digging_ability)):
                    print('\n The rat info:')
                    l = zoo.search_by_name(name=name)
            except Exception as e:
                animal_logger.error(f"validation error :{e}")
                print("\nYou gave the wrong input!")
        case "snake":
            try:
                name = input("Enter snake name:")
                weight = input("Enter snake weight(number):")
                age = input("Enter snake age(number):")
                venomous = input("Is that snake venomous?(True or False):")
                tamed = input("Is the snake tamed?(True or False):")
                length = input("Enter the length of this snake:")
                if zoo.create(animal_type="snake" , name=name , weight=float(weight) , age=int(age) , venomous=bool(venomous) , tamed=bool(tamed)  , length=float(length)):
                    print("The snake info:")
                    zoo.search_by_name(name)
            except Exception as e :
                    animal_logger.error(f"validation error :{e}")
                    print("\nYou gave the wrong input!")

        case _:
            print('\nInvalid input!')
    operations(role=role)

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
                    if permission(role=role):
                        db.save_to_db(zoo.animals_list)
                        print("\nSuccesfully saved.")
                except p.PermissionError as e:
                        animal_logger.error(f"a user try to delete an animal:{e}")
                        print(e.args[0])
            case 9:
                try:
                    if logged_in(role):
                        login()
                except p.PermissionError as e:
                        print(e.args[0])
            case 10:
                try :
                    if permission(role):
                        with open("animals.json", 'w', encoding='utf-8') as file:
                            json.dump([animal.to_json() for animal in zoo.animals_list], file)
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