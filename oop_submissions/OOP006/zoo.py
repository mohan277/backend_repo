class Deer:
    
    deers_count = 0
    sound = 'Buck Buck'
    breathing = 'Breathe in air'
    
    def __init__(self,age_in_months, breed, required_food_in_kgs):
        self._age_in_months =age_in_months
        self._breed= breed
        self._required_food_in_kgs = required_food_in_kgs
        type(self).deers_count += 1
        
        if self._age_in_months != 1:
            raise ValueError(f'Invalid value for field age_in_months: {self.age_in_months}')
            
        if self._required_food_in_kgs <= 0:
            raise ValueError(f'Invalid value for field required_food_in_kgs: {self._required_food_in_kgs}')
            
            
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 2
    
    
    def make_sound(self):
        print(type(self).sound)
    
    def breathe(self):
        print(type(self).breathing)
  
  
class Lion(Deer):
    
    sound = 'Roar Roar'
    breathing = 'Breathe in air'
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 4
    
    def hunt(self,park_name):
        self.park_name = park_name
        if type(self).deers_count > 0:
            type(self).deers_count -= 1
        else:
            print('No deers to hunt')
        
        
class Shark(Deer):
    
    sound = 'Shark Sound'
    breathing = 'Breathe oxygen from water'
    
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 8
    
        
class GoldFish(Deer):
    
    GoldFish_count = 0
    sound = 'Hum Hum'
    breathing = 'Breathe oxygen from water'
    
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 0.2

class Zoo:
    
    animals_count = 0
    
    
    def __init__(self):
        self._reserved_food_in_kgs = 0
        animals_list = []
    
    def add_food_to_reserve(self,add_food_to_reserve):
        
        if add_food_to_reserve <= 0:
            raise ValueError(f'Invalid value for add_food_to_reserve: {self.add_food_to_reserve}')
            
        self._reserved_food_in_kgs += add_food_to_reserve
    
    def add_animal(self,animal):
        # type(self).animals_list.append(animal)
        type(self).animals_count += 1
        
    def count_animals(self):
        return type(self).animals_count

    def feed(self,animal):
        
        if self._reserved_food_in_kgs >= animal.required_food_in_kgs and self._reserved_food_in_kgs > 0:
            self._reserved_food_in_kgs -= animal.required_food_in_kgs
            animal.grow()
    
    @property
    def required_food_in_kgs(self):
        return self._reserved_food_in_kgs

class Snake(Deer):
    
    sound = 'Hiss Hiss'
    breathing = 'Breathe in air'
    
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 0.5



























# lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
# deer = Deer(age_in_months=1, breed="ELK", required_food_in_kgs=10)
# shark = Shark(age_in_months=1, breed="Hunter Shark", required_food_in_kgs=10)
# lion.make_sound()
# lion.breathe()
# deer.make_sound()
# deer.breathe()
# shark.make_sound()
# shark.breathe()