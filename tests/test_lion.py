import unittest
import animal
import ExceptionHandeling as eh
class LionTest(unittest.TestCase):

    def setUp(self):
        self.animal_type = "lion"
        self.name = "name"
        self.age = 1
        self.weight = 2.5
        self.tail_size = 22.2
        self.herd_leader = True
        self.strength = 2

    def test_lion_init(self):
        animal_lion = animal.lion(animal_type=self.animal_type ,name=self.name , weight=self.weight ,
                             age=self.age , tail_size=self.tail_size , herd_leader=self.herd_leader , strength=self.strength)

        self.assertEqual(animal_lion.name, self.name)
        self.assertEqual(animal_lion._weight, self.weight)
        self.assertEqual(animal_lion.age, self.age)
        self.assertEqual(animal_lion._herd_leader , self.herd_leader)
        self.assertEqual(animal_lion._strength , self.strength)
        self.assertEqual(animal_lion._tail_size , self.tail_size)
        self.assertIsNotNone(animal_lion.id)

    def test_validation_weight_error(self):
        self.assertRaises(
            eh.InvalidInput, animal.lion  , 
            animal_type=self.animal_type,
            name=self.name,
            weight=-1.1,
            age=self.age,
            tail_size=self.tail_size,
            herd_leader=self.herd_leader,
            strength=self.strength
        )
        self.assertRaises(
            eh.InvalidInput, animal.lion  , 
            animal_type=self.animal_type,
            name=self.name,
            weight=1,
            age=self.age,
            tail_size=self.tail_size,
            herd_leader=self.herd_leader,
            strength=self.strength
        )
    def test_validation_age_error(self):
        self.assertRaises(
            eh.InvalidInput, animal.lion  , 
            animal_type=self.animal_type,
            name=self.name,
            weight=self.weight,
            age=-1,
            tail_size=self.tail_size,
            herd_leader=self.herd_leader,
            strength=self.strength
        )
        self.assertRaises(
            eh.InvalidInput, animal.lion  , 
            animal_type=self.animal_type,
            name=self.name,
            weight=self.weight,
            age="1",
            tail_size=self.tail_size,
            herd_leader=self.herd_leader,
            strength=self.strength
        )
    def test_validation_strength_error(self):
        self.assertRaises(
            eh.InvalidInput, animal.lion  , 
            animal_type=self.animal_type,
            name=self.name,
            weight=self.weight,
            age=self.age,
            tail_size=self.tail_size,
            herd_leader=self.herd_leader,
            strength="s"
        )
        self.assertRaises(
            eh.InvalidInput, animal.lion  , 
            animal_type=self.animal_type,
            name=self.name,
            weight=self.weight,
            age=self.age,
            tail_size=self.tail_size,
            herd_leader=self.herd_leader,
            strength=11
        )
        self.assertRaises(
            eh.InvalidInput, animal.lion  , 
            animal_type=self.animal_type,
            name=self.name,
            weight=self.weight,
            age=self.age,
            tail_size=self.tail_size,
            herd_leader=self.herd_leader,
            strength=-1
        )
    def test_validation_HerdLeader_error(self):
        self.assertRaises(
            eh.InvalidInput, animal.lion  , 
            animal_type=self.animal_type,
            name=self.name,
            weight=self.weight,
            age=self.age,
            tail_size=self.tail_size,
            herd_leader="ok",
            strength=self.strength
        )  
    def test_validation_TailSize_error(self):
        self.assertRaises(
            eh.InvalidInput, animal.lion  , 
            animal_type=self.animal_type,
            name=self.name,
            weight=self.weight,
            age=self.age,
            tail_size=-1.0,
            herd_leader=self.herd_leader,
            strength=self.strength
        )
        self.assertRaises(
            eh.InvalidInput, animal.lion  , 
            animal_type=self.animal_type,
            name=self.name,
            weight=self.weight,
            age=self.age,
            tail_size=1,
            herd_leader=self.herd_leader,
            strength=self.strength
        )
    def test_make_sound(self):
        lion = animal.lion(animal_type=self.animal_type , name=self.name , age=self.age , weight=self.weight , tail_size=self.tail_size , strength=self.strength , herd_leader=self.herd_leader)
        sound = lion.make_sound()
        self.assertEqual(sound , "Roar")
        

if __name__ == '__main__':
    unittest.main()