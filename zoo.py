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

    def create(self , animal_type , name , weight , age , special1 , special2 , special3):
    #ورودی special برای ویژگی منحصر به فرد هر حیوان است
        self.validation(name)
        match animal_type:
            case "lion":
                try:
                    l = animal.lion(name=name , weight=weight , age=age , taile_size=special1 , herd_leader=special2 , strength=special3)
                    self.animals_list.append(l)
                    return True
                except eh.InvalidInput as e:
                    print(e.args[0])
                
            case "rat":
                try:
                    r = animal.rat(name=name , weight=weight , age=age , color=special1 , climbing_ability=special2 , digging_ability=special3)
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
# my_zoo.create( animal_type='lion' , name="aa",weight=32 , age=1 , special1=1 , special2=False , special3=1)
# my_zoo.create(animal_type="rat" , name="aa" , weight=32 , age=1 , special1="green" , special2=False , special3=True)
# my_zoo.ShowList()
# l = my_zoo.animals_list[0]
# print(l)
# print(l.climbing_ability )
# l.climbing_ability=True
# print(l.climbing_ability )
# print(l.digging_ability)
# l.digging_ability = False
# print(l.digging_ability)
# p = my_zoo.GetIdByName("aa")

