class Car:
    
    HORN_SOUND = 'Beep Beep'
    
    def __init__(self,color=None, max_speed=None, acceleration=None, tyre_friction=None):
        self._color = color
        self._max_speed = max_speed
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._is_engine_started = False
        self._current_speed = 0
        
        self.raiseError(self._max_speed, 'max_speed')
        self.raiseError(self._acceleration, 'acceleration')
        self.raiseError(self._tyre_friction, 'tyre_friction')
        
    @property
    def color(self):
        return self._color
            
    @property
    def max_speed(self):
        return self._max_speed
            
    @property
    def acceleration(self):
        return self._acceleration
            
    @property
    def tyre_friction(self):
        return self._tyre_friction
        
    @property
    def is_engine_started(self):
        return self._is_engine_started
        
    @property
    def current_speed(self):
        return self._current_speed
    
    @staticmethod
    def raiseError(value,name):
        if value <= 0:
            raise ValueError(f'Invalid value for {name}')
            
    
    def start_engine(self):
        if self._is_engine_started == False:
            self._is_engine_started = True
    
    
    def sound_horn(self):
        if self._is_engine_started:
            print(type(self).HORN_SOUND)
        else:
            print('Start the engine to sound_horn')
    
    def accelerate(self):
        if self._is_engine_started:
            if self._current_speed + self._acceleration <= self._max_speed:
                self._current_speed += self._acceleration
            else:
                self._current_speed = self._max_speed
        else:
            print('Start the engine to accelerate')
            
    def apply_brakes(self):
        if self._current_speed >= self._tyre_friction:
            self._current_speed -= self._tyre_friction
        else:
            self._current_speed = 0
    
    def stop_engine(self):
        if self._is_engine_started == True:
            self._is_engine_started = False
        
    
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
        
    
class RaceCar(Car):
    HORN_SOUND = 'Peep Peep\nBeep Beep'
    
    def __init__(self,color=None, max_speed=None, acceleration=None, tyre_friction=None):
        super().__init__(color, max_speed, acceleration,tyre_friction)
        self._nitro = 0
        
    @property
    def nitro(self):
        return self._nitro
    
    def apply_brakes(self):
        if self._current_speed >= self._tyre_friction:
            if self._current_speed > self._max_speed/2:
                self._nitro += 10
            self._current_speed -= self._tyre_friction
        else:
            self._current_speed = 0
            
            
    def accelerate(self):
        import math
        if self._is_engine_started:
            if self._nitro > 0:
                self._nitro -= 10
                if self._current_speed + self._acceleration + (math.ceil(self._acceleration * 30/100)) <= self._max_speed:
                    self._current_speed += self._acceleration + (math.ceil(self._acceleration * 30/100))
                else:
                    self._current_speed = self._max_speed
            else:
                super().accelerate()
        else:
            print('Start the engine to accelerate')