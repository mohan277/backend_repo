class Car:
    def __init__(self,color='Red' , max_speed = 250, acceleration = 10,tyre_friction = 7):
        self._color = color
        self._max_speed = max_speed
        
        if self._max_speed < 0:
            myError = ValueError('Invalid value for max_speed')
            raise myError
        self._acceleration = acceleration
        
        if self._acceleration < 0:
            myError = ValueError('Invalid value for acceleration')
            raise myError
        self._tyre_friction = tyre_friction
        
        if self._tyre_friction < 0:
            myError = ValueError('Invalid value for tyre_friction')
            raise myError
        self._current_speed = 0
        self._is_engine_started = False
        
    @property
    def color(self):
        return self._color
    @property
    def current_speed(self):
        return self._current_speed
    
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
        
    def start_engine(self):
        self._is_engine_started = True
        return self._is_engine_started
        
    def accelerate(self):
        if self._is_engine_started == True:
            self._current_speed += self._acceleration
        else:
            print('Start the engine to accelerate')
        if self._current_speed > self._max_speed:
            self._current_speed = self._max_speed
    
    def apply_brakes(self):
        if self._current_speed > self._tyre_friction:
            self._current_speed -= self._tyre_friction
        else:
            self._current_speed = 0
        if self._current_speed < 0:
            self._current_speed = 0
    
    def sound_horn(self):
        if self._is_engine_started == True:
            print('Beep Beep')
        else:
            print('Start the engine to sound_horn')
            
    def stop_engine(self):
        if self._is_engine_started == True:
            self._is_engine_started = False
            return self._is_engine_started

class Truck(Car):
    
    def __init__(self,color = 'Black', max_speed = 250, acceleration = 10,tyre_friction = 7,max_cargo_weight = 100):
        super().__init__(color, max_speed, acceleration,tyre_friction)
        
        self._max_cargo_weight = max_cargo_weight
        self.mycargo = 0
        
        if self._max_cargo_weight < 0:
            myError = ValueError('Invalid value for max_cargo_weight')
            raise myError
            
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    
    def sound_horn(self):
        if self._is_engine_started == True:
            print('Honk Honk')
        else:
            print('Start the engine to sound_horn')
            
    def load(self,cargo_weight):
        
        if cargo_weight < 0:
            myError = ValueError('Invalid value for cargo_weight')
            raise myError
            
        if self._current_speed == 0:
            self.mycargo += cargo_weight
            if self.mycargo > self._max_cargo_weight:
                print(f'Cannot load cargo more than max limit: {self._max_cargo_weight}')
                self.mycargo -= cargo_weight
        else:
            print('Cannot load cargo during motion')
    
    def unload(self,cargo_weight):
        if cargo_weight < 0:
            myError = ValueError('Invalid value for cargo_weight')
            raise myError
            
        if self._current_speed == 0:
            self.mycargo -= cargo_weight
        else:
            print('Cannot unload cargo during motion')

class RaceCar(Car):
    def __init__(self,color = 'Blue', max_speed = 300, acceleration = 20,tyre_friction = 10):
        super().__init__(color, max_speed, acceleration,tyre_friction)
        self._nitro = 0
            
    @property    
    def nitro(self):
        return self._nitro
        
    def sound_horn(self):
        if self._is_engine_started == True:
            print('Peep Peep\nBeep Beep')
        else:
            print('Start the engine to sound_horn')
            
    def apply_brakes(self):
        if self._current_speed > self._max_speed/2:
            self._nitro += 10
        if self._current_speed > self._tyre_friction:
            self._current_speed -= self._tyre_friction
        else:
            self._current_speed = 0
        if self._current_speed < 0:
            self._current_speed = 0
    
    def accelerate(self):
        import math
        if self._is_engine_started == True:
            if self._nitro > 0:
                self._current_speed += int(math.ceil(self._acceleration*1.3))
                self._nitro -= 10
            else:
                self._current_speed += self._acceleration
            if self._current_speed > self._max_speed:
                self._current_speed = self._max_speed
        else:
            print('Start the engine to accelerate')



truck = Truck(color="Red", max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=150)  
truck.load(50)  
truck.load(100)  
# truck.load(-100) 

# 01efa9b4e2f647ed98d2b0a1b180c3a7/test_truck.py::test_load_cargo_when_current_truck_load_is_more_than_max_limit_and_is_at_rest: failed   