import animal
import ExceptionHandeling as eh


def create_animal(animal_type , name , weight , age , **kwargs):
    match animal_type:
        case "lion":
            return animal.lion(animal_type=animal_type , name=name , weight=weight , age=age , **kwargs)
            
        case "rat":
            return animal.rat(animal_type=animal_type , name=name , weight=weight , age=age , **kwargs)
        case "snake":
            return animal.snake(animal_type=animal_type , name=name , weight=weight , age=age , **kwargs)
        case _:
            eh.raise_error(7)


class Zoo:
    def __init__(self):
        # self.create(self , animal_type , name , weight , age  , special)
        self.animals_list = []
    
    def validation(self , name):
        for i in self.animals_list:
            if i.name == name :
                eh.raise_error(9)

    def create(self , animal_type , name , weight , age , **kwargs):
        try:
            self.validation(name)
            animal = create_animal(animal_type , name , weight , age , **kwargs)
            print(animal)
            self.animals_list.append(animal)
            return True
        except eh.InvalidInput as e:
            print("\n",e.args[0])
            return False            

    def destroy(self , name):
        for AnimalObject in self.animals_list :

            if AnimalObject.name == name :
                AnimalObject.info()
                i = input("\nare you sure you want to destroy this animal ( y / n ) :")
                if i == 'y':
                    self.animals_list.remove(AnimalObject)
                    del AnimalObject
                    print('the animal succsesfully destroyed')
                    return True
                elif i == 'n':
                    print('ok')
                    return False                    
                else:
                    print('\ninvalid input!')
                    return False
        print("\ninvalid input!")
        return False
    
    def ShowList(self):
        if len(self.animals_list) != 0:
            for AnimalObject in self.animals_list:
                print("\n")
                AnimalObject.info()
        else :
            print("\nThere is no animal in the zoo")

    def search_by_id(self , id):
        for AnimalObject in self.animals_list:
            if AnimalObject.id == int(id):
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
