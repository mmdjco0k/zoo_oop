admin_username = "admin"
admin_password = "admin123"

def print_menu(status):    
    match status:
        case "start":
            print('\n1 : login as admin')
            print('2 : enter as user (no login requierd)')
        case "admin":
            print('\n1 : add animal')
            print('2 : delete animal')
            print('3 : show all animal')
            print('4 : search by the name or id')
            print('5 : counting the number of animals of each species')
            print('6 : get log')
            print('7 : save and recover data')
        case "user":
            print('\n1 : show all animal')
            print('2 : search by the name or id')
            print('3 : counting the number of animals of each species')

def admin():
    while True:
        operation = int(input("\nenter a number : "))

        match operation:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case _:
                print("\ninvalid input!")

def user():
    while True:
        operation = int(input("\nenter a number : "))

        match operation:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case _:
                print("\ninvalid input!")

def login():
    while True:
        print_menu('start')
        user_input = int(input("\nEnter a number : "))
        match user_input:
            case 1:
                username = input("\nenter username : ")
                password = input("enter password : ")
                if (username == admin_username and admin_password == admin_password) :
                    print_menu("admin")
                    admin()
                    break
                else :
                    print("\nusername or password is wrong!")

            case 2:
                print_menu('user')
                user()
                break
            case _:
                print('\nyour input is invalid!s')

