class Animal:
    SOUND = ''
    BREATHE = ''
    Increase_in_food = 0
    
    def __init__(self, age_in_months=None, breed=None, required_food_in_kgs=None):
        self._age_in_months = age_in_months
        self._required_food_in_kgs = required_food_in_kgs
        self._breed = breed
        
        self.raiseError(self._age_in_months, 'age_in_months')
        self.raiseError(self._required_food_in_kgs, 'required_food_in_kgs')
        
    @staticmethod
    def raiseError(value,name):
        if name == 'age_in_months' and value != 1:
            raise ValueError(f'Invalid value for {name}: {value}')
        elif name == 'required_food_in_kgs' and value <= 0:
            raise ValueError(f'Invalid value for {name}: {value}')
        
    @property
    def age_in_months(self):
        return self._age_in_months
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    @property
    def breed(self):
        return self._breed
    
    @classmethod
    def make_sound(cls):
        print(cls.SOUND)
    @classmethod
    def breathe(cls):
        print(cls.BREATHE)
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += type(self).Increase_in_food

class Deer(Animal):
    SOUND = 'Buck Buck'
    BREATHE = 'Breathe in air'
    Increase_in_food = 2
    
class Lion(Animal):
    SOUND = 'Roar Roar'
    BREATHE = 'Breathe in air'
    Increase_in_food = 4
    
    
class Shark(Animal):
    SOUND = 'Shark Sound'
    BREATHE = 'Breathe oxygen from water'
    Increase_in_food = 8
    
    
class GoldFish(Animal):
    SOUND = 'Hum Hum'
    BREATHE = 'Breathe oxygen from water'
    Increase_in_food = 0.2
    
    
class Snake(Animal):
    SOUND = 'Hiss Hiss'
    BREATHE = 'Breathe in air'
    Increase_in_food = 0.5
    
class Zoo(Animal):
    
    animals_count = 0
    
    def __init__(self):
        self._reserved_food_in_kgs =0
        
    
    @property
    def reserved_food_in_kgs(self):
        return self._reserved_food_in_kgs
    
    def add_food_to_reserve(self,add_food_to_reserve):
        self._reserved_food_in_kgs += add_food_to_reserve
    
    def count_animals(self):
        return type(self).animals_count
    
    def add_animal(self,animal_name):
        type(self).animals_count += 1
        
    def feed(self,animal_name):
        
        if self._reserved_food_in_kgs >= animal_name._required_food_in_kgs:
            self._reserved_food_in_kgs -= animal_name._required_food_in_kgs
            animal_name.grow()
    
    @classmethod
    def count_animals_in_all_zoos(cls):
        passc
    
        @classmethod
    def count_animals_in_all_zoos(cls):
        passc

    
zoo = Zoo()

print(zoo.reserved_food_in_kgs)
zoo.add_food_to_reserve(10000000)
print(zoo.reserved_food_in_kgs)

gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
zoo.add_animal(gold_fish)
print(zoo.count_animals())

print(zoo.reserved_food_in_kgs)
zoo.feed(gold_fish)
print(zoo.reserved_food_in_kgs)
zoo.feed(gold_fish)
zoo.feed(gold_fish)
zoo.feed(gold_fish)
print(gold_fish.age_in_months)
print(zoo.reserved_food_in_kgs)