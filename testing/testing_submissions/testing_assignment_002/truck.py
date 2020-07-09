from car import Car

class Truck(Car):
    
    HORN_SOUND = 'Honk Honk'
    def __init__(self,color=None, max_speed=None, acceleration=None, tyre_friction=None, max_cargo_weight=None):
        super().__init__(color, max_speed, acceleration,tyre_friction)
        self._max_cargo_weight = max_cargo_weight
        self._my_cargo = 0
    
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    @property
    def may_cargo(self):
        return self._my_cargo
        
    @property
    def cargo_weight(self):
        return self._cargo_weight
    
    def load(self, cargo_weight):
        if self._current_speed <= 0:
            self._cargo_weight = cargo_weight
            if self._cargo_weight <= 0:
                raise ValueError(f'Invalid value for cargo_weight')
            else:
                if self._my_cargo + self._cargo_weight <= self._max_cargo_weight:
                    self._my_cargo += self._cargo_weight
                else:
                    print(f'Cannot load cargo more than max limit: {self._max_cargo_weight}')
        else:
            print('Cannot load cargo during motion')
            
            
    def unload(self, cargo_weight):
        if self._current_speed <= 0:
            self._cargo_weight = cargo_weight
            if self._cargo_weight <= 0:
                raise ValueError(f'Invalid value for cargo_weight')
            else:
                if self._my_cargo - self._cargo_weight >= 0:
                    self._my_cargo -= self._cargo_weight
        else:
            print('Cannot unload cargo during motion')
