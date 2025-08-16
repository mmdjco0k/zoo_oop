class PermissionError(Exception):
    def __init__(self, message="\nYou dont have permission to perform this operation!"):
        super().__init__(message)

def raise_permission_error(exeption_id):
        exeption_id = exeption_id
        match exeption_id:
            case 1:
                raise PermissionError()
            case 2:
                raise PermissionError(message="\nyou allready logged in!")



class custom_permission:
    def __init__(self):
        self.permissions = {
            'admin': ['create', 'destroy', 'show_list', 'search_by_id', 'search_by_name'],
            'user': ['show_list', 'search_by_id', 'search_by_name'],}
    
    def has_permission(self , role , method_name):
        if method_name not in self.permissions[role]:
            print(self.permissions[role])
            print(method_name)
            raise_permission_error(1)
        return True

    @staticmethod
    def logged_in(role):
        if role == "user":
            return False
        raise_permission_error(2)