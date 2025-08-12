import unittest
import animal
import ExceptionHandeling as eh

class RatTest(unittest.TestCase):

    def setUp(self):
        self.animal_type = "rat"
        self.name = "name"
        self.age = 1
        self.weight = 2.5
        self.color = "red"
        self.climbing_ability = True
        self.digging_ability = False

    def test_lion_init(self):
        animal_rat = animal.rat(animal_type=self.animal_type ,name=self.name , weight=self.weight ,
                             age=self.age , color=self.color , 
                             climbing_ability=self.climbing_ability , digging_ability=self.digging_ability)

        self.assertEqual(animal_rat.name, self.name)
        self.assertEqual(animal_rat._weight, self.weight)
        self.assertEqual(animal_rat.age, self.age)
        self.assertEqual(animal_rat._color , self.color)
        self.assertEqual(animal_rat._climbing_ability , self.climbing_ability)
        self.assertEqual(animal_rat._digging_ability , self.digging_ability)
        self.assertIsNotNone(animal_rat.id)
    
    def test_validation_climbing_ability(self):
        self.assertRaises(eh.InvalidInput , animal.rat ,
            animal_type=self.animal_type,
            name=self.name,
            weight=self.weight,
            age=self.age,
            climbing_ability="W",
            digging_ability=self.digging_ability,
            color=self.color
        )

    def test_validation_digging_ability(self):
        self.assertRaises(eh.InvalidInput , animal.rat ,
            animal_type=self.animal_type,
            name=self.name,
            weight=self.weight,
            age=self.age,
            climbing_ability=self.climbing_ability,
            digging_ability=2,
            color=self.color
        )
    
    def test_make_sound(self):
        animal_rat = animal.rat(animal_type=self.animal_type ,name=self.name , weight=self.weight ,
                             age=self.age , color=self.color , 
                             climbing_ability=self.climbing_ability , digging_ability=self.digging_ability)
        sound = animal_rat.make_sound()
        self.assertEqual(sound , "hisses")

    
if __name__ == "__main__":
    unittest.main()