class Deer:
    
    deers_count = 0
    sound = 'Buck Buck'
    breathing = 'Breathe in air'
    
    def __init__(self,age_in_months=None, breed=None, required_food_in_kgs=None):
        self._age_in_months =age_in_months
        self._breed= breed
        self._required_food_in_kgs = required_food_in_kgs
        type(self).deers_count += 1
        
        if self._age_in_months != 1:
            raise ValueError(f'Invalid value for field age_in_months: {self._age_in_months}')
            
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
            print(type(self).deers_count)
        else:
            print('No deers to hunt')
