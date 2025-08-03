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