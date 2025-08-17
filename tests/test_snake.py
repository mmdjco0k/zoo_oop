import unittest
import ExceptionHandeling as eh
from animals.snake import Snake

class SnakeTest(unittest.TestCase):
    def setUp(self):
        self.animal_type = "snake"
        self.name = "name"
        self.age = 1
        self.weight = 2.5
        self.venomous = True
        self.tamed = False
        self.length = 2.2
    
    def test_snake_init(self):
        snake = Snake(animal_type=self.animal_type , name=self.name , age=self.age , weight=self.weight ,
                venomous=self.venomous , tamed=self.tamed , length=self.length
        )

        self.assertEqual(snake.name, self.name)
        self.assertEqual(snake._weight, self.weight)
        self.assertEqual(snake.age, self.age)
        self.assertEqual(snake._venomous , self.venomous)
        self.assertEqual(snake._tamed , self.tamed)
        self.assertEqual(snake._length , self.length)
        self.assertIsNotNone(snake.id)

    def test_validation_venomous_error(self):

        self.assertRaises(eh.InvalidInput , Snake ,
            animal_type=self.animal_type,
            name=self.name,
            weight=self.weight,
            age=self.age,
            venomous="no",
            tamed=self.tamed,
            length=self.length
        )

    def test_validation_tamed_error(self):

        self.assertRaises(eh.InvalidInput , Snake ,
            animal_type=self.animal_type,
            name=self.name,
            weight=self.weight,
            age=self.age,
            venomous=self.venomous,
            tamed=2,
            length=self.length
        )
    
    def test_validation_length_error(self):
        self.assertRaises(eh.InvalidInput , Snake ,
            animal_type=self.animal_type,
            name=self.name,
            weight=self.weight,
            age=self.age,
            venomous=self.venomous,
            tamed=self.tamed,
            length=2
        )
    
    def test_make_sound(self):
        snake = Snake(animal_type=self.animal_type , name=self.name , age=self.age , weight=self.weight ,
                venomous=self.venomous , tamed=self.tamed , length=self.length)
        sound = snake.make_sound()
        self.assertEqual(sound , "sisss")

if __name__ == '__main__':
    unittest.main()