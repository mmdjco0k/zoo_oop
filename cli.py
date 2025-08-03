import permission as p
admin_username = "admin"
admin_password = "admin123"

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
            print('4 : search by the name or id')
            print('5 : counting the number of animals of each species')
            print('6 : get log')
            print('7 : save and recover data')
            print('8 : login')
            operation = int(input("\nenter a number : "))
            return operation


def operations(role):
    while True:
        operation = print_menu('operations')
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
            case 8:
                try:
                    if logged_in(role):
                        login()
                except p.PermissionError as e:
                        print(e.args[0])
            case _:
                print("\ninvalid input!")


def login():
    role = 'user'
    while True:
        user_input = print_menu('start')
        match user_input:
            case 1:
                username = input("\nenter username : ")
                password = input("enter password : ")
                if (username == admin_username and admin_password == admin_password) :
                    # print_menu("admin")
                    role = 'admin'
                    operations(role=role)
                    break
                else :
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