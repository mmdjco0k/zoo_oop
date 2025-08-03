import animal
import ExceptionHandeling as eh
class Zoo:
    def __init__(self):
        # self.create(self , animal_type , name , weight , age  , special)
        self.animals_list = []
    
    def validation(self , name):
        for i in self.animals_list:
            if i.name == name :
                eh.raise_error(9)

    def create(self , animal_type , name , weight , age , special1 , special2 , special3):
    #ورودی special برای ویژگی منحصر به فرد هر حیوان است
        try:
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
                        s = animal.snake(name=name , weight=weight , age=age , venomous=special1 , tamed=special2 , length=special3)
                        self.animals_list.append(s)
                        return True
                    except eh.InvalidInput as e:
                        print(e.args[0])

                case _:
                    error = animal.InvalidAnimalDataException(7)
                    error.run_exeption()
                    return False
        except eh.InvalidInput as e:
                        print("\n",e.args[0])

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
                    print('\ninvalid input!')
                    return False
        print("\ninvalid id!")
        return False
    
    def ShowList(self):
        for AnimalObject in self.animals_list:
            print("\n")
            AnimalObject.info()

    def search_by_id(self , id):
        for AnimalObject in self.animals_list:
            if AnimalObject.id == id:
                AnimalObject.info()
                return AnimalObject
        print('\ninvalid input!')
        return False

    def search_by_name(self , name):
        for AnimalObject in self.animals_list:
            if AnimalObject.name == name :
                AnimalObject.info()
                return AnimalObject
        print('\ninvalid input!')
        return False
 
    def counter(self):
        lion_counter = 0
        rat_counter = 0
        snake_counter = 0
        for AnimalObject in self.animals_list:
            if AnimalObject.animal_type == "lion":
                lion_counter += 1
            elif AnimalObject.animal_type == "rat":
                rat_counter += 1
            elif AnimalObject.animal_type == "snake":
                snake_counter += 1
        print(f"We have {lion_counter} of lions")
        print(f"We have {rat_counter} of rats")
        print(f"We have {snake_counter} of snakes")

    
# my_zoo = Zoo()
# my_zoo.create(animal_type="lion" , name="aa" , weight=32.0 , age=21 , special1=11.1 , special2=True , special3=10)
# my_zoo.create(animal_type="lion" , name="aa" , weight=32.0 , age=21 , special1=11.1 , special2=True , special3=10)
# my_zoo.create(animal_type="rat" , name="s" , weight=32.0 , age=21 , special1="green" , special2=True , special3=False)
# my_zoo.create(animal_type="snake" , name="f" , weight=32.0 , age=21 , special1=True , special2=False , special3=11.1)


# my_zoo.ShowList()
# l = my_zoo.animals_list[0]
# print(l) 

# l = my_zoo.counter()
# print(l)

