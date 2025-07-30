import animal

class Zoo:
    def __init__(self):
        # self.create(self , animal_type , name , weight , age  , special)
        self.animals_list = []

    def create(self , animal_type , name , weight , age , special):
    #ورودی special برای ویژگی منحصر به فرد هر حیوان است
        match animal_type:
            case "lion":
                l = animal.lion(name=name , weight=weight , age=age , taile_size=special)
                self.animals_list.append(l)
            
            case "rat":
                r = animal.rat(name=name , weight=weight , age=age , color=special)
                self.animals_list.append(r)

            case "snake":
                s = animal.snake(name=name , weight=weight , age=age , venomous=special)
                self.animals_list.append(s)
            
            case _:
                error = animal.InvalidAnimalDataException(7)
                error.run_exeption()

# my_zoo = Zoo()
# my_zoo.create( animal_type='rat' , name="abas",weight=32 , age=1 , special=1)

# my_zoo.create( animal_type='lion' , name="asdwabas",weight=32 , age=1 , special=1)

# for i in my_zoo.animals_list:
#     print(i.name)
#     print(i.id)
#     print(i.animal_type)
#     i.animal_type = "x"
#     print(i.animal_type)
    
