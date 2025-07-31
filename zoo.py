import animal

class Zoo:
    def __init__(self):
        # self.create(self , animal_type , name , weight , age  , special)
        self.animals_list = []
    
    def validation(self , name):
        for i in self.animals_list:
            if i.name == name :
                error = animal.InvalidAnimalDataException(9)
                error.run_exeption()
    
    def GetIdByName(self , name):
        for AnimalObject in self.animals_list:
            if AnimalObject.name == name:
                Id = AnimalObject.id
                return Id

    def create(self , animal_type , name , weight , age , special):
    #ورودی special برای ویژگی منحصر به فرد هر حیوان است
        self.validation(name)
        match animal_type:
            case "lion":
                l = animal.lion(name=name , weight=weight , age=age , taile_size=special)
                self.animals_list.append(l)
                return True
            
            case "rat":
                r = animal.rat(name=name , weight=weight , age=age , color=special)
                self.animals_list.append(r)
                return True

            case "snake":
                s = animal.snake(name=name , weight=weight , age=age , venomous=special)
                self.animals_list.append(s)
                return True

            case _:
                error = animal.InvalidAnimalDataException(7)
                error.run_exeption()
                return False


    def destroy(self , id):
        for AnimalObject in self.animals_list :
            if AnimalObject.id == id :
                AnimalObject.info()
                i = input("\nare you sure you want to destroy this animal ( y / n ) :")
                if i == 'y':
                    self.animals_list.remove(AnimalObject)
                    del AnimalObject
                    print('the animal succsesfully destroyed')
                    return True
                elif i == 'n':
                    return False                    
                else:
                    print('invalid input!')
                    return False
            else :
                print("invalid id!")
                return False
                


    
