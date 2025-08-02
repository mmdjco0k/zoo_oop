class errors(Exception):
    pass

class InvalidInput(errors):
    def __init__(self, message="Invalid input provided"):
        super().__init__(message)

class IdException(errors):
    def __init__(self , message = "you cannot change id"):
        super().__init__(message)

class PrivateVarException(errors):
    def __init__(self , message = "there is problem"):
        super().__init__(message)

def raise_error(exeption_id):
        exeption_id = exeption_id
        match exeption_id:
            case 1:
                raise InvalidInput(message = "\nThe weight must be positive!")
            case 2:
                raise InvalidInput(message = "\nage cannot be negative!")
            case 3:
                raise IdException(message="\nyou can not change id!")
            case 4:
                raise PrivateVarException(message = "\nthere is a problem!")
            case 6:
                raise InvalidInput(message = "\ntail size cannot be negative!")
            case 7 :
                raise InvalidInput(message = "\nthe animal type is wrong!")
            case 8:
                raise PrivateVarException(message = "\nyou cannot change animal type!")
            case 9:
                raise InvalidInput(message = "\nthe animal name is taken!")
            case 10 :
                raise InvalidInput(message="\nStrength should be between 1 and 10!")
            case 11:
                    raise InvalidInput(message="\nThis value should be boolean (True or False)!")
            case 12:
                    raise InvalidInput(message = "\nThe tail size must be positive!")




