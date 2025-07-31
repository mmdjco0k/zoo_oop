import animal
import ExceptionHandeling as eh
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
                try:
                    l = animal.lion(name=name , weight=weight , age=age , taile_size=special)
                    self.animals_list.append(l)
                    return True
                except eh.InvalidInput as e:
                    print(e.args[0])
                
            case "rat":
                try:
                    r = animal.rat(name=name , weight=weight , age=age , color=special)
                    self.animals_list.append(r)
                    return True
                except eh.InvalidInput as e:
                        print(e.args[0])

            case "snake":
                try:
                    s = animal.snake(name=name , weight=weight , age=age , venomous=special)
                    self.animals_list.append(s)
                    return True
                except eh.InvalidInput as e:
                    print(e.args[0])

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
    
    def ShowList(self):
        for AnimalObject in self.animals_list:
            print("\n")
            AnimalObject.info()


    
# my_zoo = Zoo()
# my_zoo.create( animal_type='rat' , name="abas",weight=32 , age=1 , special=1)

# my_zoo.ShowList()

# my_zoo.create( animal_type='lion' , name="awds",weight=-32 , age=1 , special=1)

# my_zoo.ShowList()

# for i in my_zoo.animals_list:
#     print(i.name)
#     print(i.id)
#     print(i.animal_type)
#     i.animal_type = "x"
#     print(i.animal_type)