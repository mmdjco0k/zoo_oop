from CustomLogger import CustomLogger

animal_logger = CustomLogger('animal.log')


admin_username = "admin"
admin_password = "admin123"

def print_menu():
    print('\n1 : login as admin')
    print('2 : enter as user (no login requierd)')
    user_input = int(input("\nEnter a number : "))
    return user_input

def login():
    role = 'user'
    while True:
        user_input = print_menu()
        match user_input:
            case 1:
                username = input("\nenter username : ")
                password = input("enter password : ")
                if (username == admin_username and password == admin_password) :
                    role = 'admin'
                    animal_logger.info("admin logged in")
                    return role
                    break
                else :
                    animal_logger.warning("somone tried to login!")
                    print("\nusername or password is wrong!")

            case 2:
                return role
                break
            case _:
                print('\nyour input is invalid!s')