class Car:
    def __init__(self, max_speed=None, acceleration=None, tyre_friction=None, color= None):
        self._color = color
        self._max_speed = max_speed
        if self._max_speed < 0 :
            raise ValueError('Invalid value for max_speed')
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._current_speed = 0
        self._is_engine_stared = False
        self._is_brakes_applied = False
    
    def start_engine(self):
        self._is_engine_stared = True
            
    def accelerate(self):
        self.if_brakes_applied = False
        if self._is_engine_stared == True:
            if self._current_speed <= self._max_speed:
                self._current_speed += self._acceleration
        else:
            print('Start the engine to accelerate')
    
    def apply_brakes(self):
        self._is_brakes_applied = True
        if self.current_speed < 0:
            self.current_speed = 0
        else:
            self._current_speed -= self._tyre_friction
        
    def sound_horn(self):
        if self._is_engine_stared == True:
            print('Beep Beep')
        else:
            print('Start the engine to sound_horn')
        
    def stop_engine(self):
        self._is_engine_stared = False
    
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
    def current_speed(self):
        return self._current_speed
    
    @property
    def is_engine_stared(self):    
        return self._is_engine_stared
    
    @property
    def is_brakes_applied(self):
        return self._is_brakes_applied
    
class Truck(Car):
    
    def __init__(self, color, max_speed, acceleration, tyre_friction, max_cargo_weight):
        super().__init__(max_speed, acceleration, tyre_friction, color=None)
        self._max_cargo_weight = max_cargo_weight
    
    def sound_horn(self):
        if self._is_engine_stared == True:
            print('Honk Honk')
        else:
            print('Start the engine to sound_horn')
    def load(self,load_value):
        self._ld_vl = load_value
        # print(load_value)
        if self._current_speed > 0 :
                print('Cannot load cargo during motion')
        else:
            if self._ld_vl < 0 :
                raise ValueError('Invalid value for cargo_weight')
            else:
                if self._ld_vl < self._max_cargo_weight:
                    self._ld_vl += self._ld_vl
                else:
                    print('Cannot load cargo more than max limit: %s' %self._max_cargo_weight)
        
    @property
    def max_cargo_weight(self):    
        return self._max_cargo_weight
    
    @property
    def ld_vl(self):    
        return self._max_cargo_weight

class RaceCar(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        super().__init__(max_speed, acceleration, tyre_friction, color=None)
        self._nitro = 0
    def sound_horn(self):
        if self._is_engine_stared == True:
            print('Peep Peep\nBeep Beep')
        else:
            print('Start the engine to sound_horn')

    def accelerate(self):
        self._is_brakes_applied = False
        if self._is_engine_stared == True:
            if self._current_speed <= self._max_speed:
                self._current_speed += self._acceleration
            if self._current_speed <= self._max_speed and self._is_brakes_applied:
                self._current_speed += self._acceleration + (self._acceleration * 30//100)
                self._nitro = 0
            if self.current_speed > self._max_speed//2:
                self._nitro = 10
        else:
            print('Start the engine to accelerate')
        
    @property
    def nitro(self):    
        return self._nitro


car = Car(max_speed=250, acceleration=10, tyre_friction=3, color="Red")
truck = Truck(max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100, color="Red")
racecar = RaceCar(max_speed=250, acceleration=50, tyre_friction=30, color="Red")








# print(car.acceleration)
# print(car.tyre_friction)
# print(car.max_speed)
# print(car.color)

# print(truck.acceleration)
# print(truck.tyre_friction)
# print(truck.max_speed)
# print(truck.color)

# print(car.is_engine_stared)
# car.start_engine()
# print(car.is_engine_stared)

# print(car.current_speed)

# car.start_engine()  
# car.accelerate()
# print(car.current_speed)
# car.accelerate()
# print(car.current_speed)

# car.accelerate()

# car.start_engine()  
# car.accelerate()
# print(car.current_speed)
# car.apply_brakes()  
# print(car.current_speed)

# car.start_engine()  
# car.sound_horn()

# car.sound_horn()

# car.start_engine()  
# print(car.is_engine_stared)
# car.stop_engine()  
# print(car.is_engine_stared)

# car.current_speed
# car.start_engine()
# print(car.current_speed)
# car.current_speed = 10

# truck.load(50)  
# truck.load(100)
# truck.load(-100)

# truck.start_engine()
# truck.accelerate()
# truck.load(50)

# truck.start_engine()
# truck.sound_horn()

racecar.start_engine()  
racecar.accelerate()  
racecar.accelerate()  
racecar.accelerate()
print(racecar.current_speed)

# racecar.apply_brakes()
# print(racecar.current_speed)

print(racecar.nitro)

# racecar.accelerate()
# print(racecar.current_speed)
# print(racecar.nitro)
# car.sound_horn()




# ________new_________


class Car:
    def __init__(self, max_speed, acceleration, tyre_friction, color= None):
        self._color = color
        self._max_speed = max_speed
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._current_speed = 0
        self._is_engine_stared = False
    
        if self._max_speed < 0 :
            myError = ValueError('Invalid value for max_speed')
            raise myError
        if self._acceleration < 0 :
            myError = ValueError('Invalid value for acceleration')
            raise myError
        if self._tyre_friction < 0:
            myError = ValueError('Invalid value for tyre_friction')
            raise myError
        
    def start_engine(self):
        self._is_engine_stared = True
        return self._is_engine_stared
        
    def accelerate(self):
        if self._is_engine_stared == True:
            if self._current_speed <= self._max_speed:
                self._current_speed += self._acceleration
            else:
                self._current_speed = self._max_speed
        else:
            print('Start the engine to accelerate')
    
    def apply_brakes(self):
        if self._current_speed < 0:
            self._current_speed = 0
        elif self._current_speed > self._tyre_friction:
            self._current_speed -= self._tyre_friction
        else:
            self._current_speed = 0
            
    def sound_horn(self):
        if self._is_engine_stared == True:
            print('Beep Beep')
        else:
            print('Start the engine to sound_horn')
        
    def stop_engine(self):
        if self._is_engine_stared == True:
            self._is_engine_stared = False
            return self._is_engine_stared
        
    
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
    def current_speed(self):
        return self._current_speed
    
    @property
    def is_engine_stared(self):    
        return self._is_engine_stared
        
    
class Truck(Car):
    
    def __init__(self, color, max_speed, acceleration, tyre_friction, max_cargo_weight):
        super().__init__(max_speed, acceleration, tyre_friction, color=None)
        self._max_cargo_weight = max_cargo_weight
        if self._max_cargo_weight < 0:
            myError = ValueError('Invalid value for max_cargo_weight')
            raise myError
            
    def sound_horn(self):
        if self._is_engine_stared == True:
            print('Honk Honk')
        else:
            print('Start the engine to sound_horn')
            
    def load(self,load_value):
        
        if load_value < 0 :
            myError = ValueError('Invalid value for max_cargo_weight')
            raise myError
        if self._is_engine_stared == False:
            self._ld_vl += self._ld_vl
                print('Cannot load cargo during motion')
        else:
            
            else:
                if self._ld_vl < self._max_cargo_weight:
                    
                else:
                    print('Cannot load cargo more than max limit: %s' %self._max_cargo_weight)
    
    def unload(self,unload_value):
        self._un_ld_vl = unload_value
        if self._current_speed > 0 :
                print('Cannot unload cargo during motion')
        else:
            if self._un_ld_vl < 0 :
                raise ValueError('Invalid value for cargo_weight')
            else:
                if self._un_ld_vl < self._max_cargo_weight:
                    self._un_ld_vl -= self._un_ld_vl
    
    @property
    def max_cargo_weight(self):    
        return self._max_cargo_weight
    
    @property
    def ld_vl(self):    
        return self._ld_vl
    
    @property
    def un_ld_vl(self):    
        return self._un_ld_vl

class RaceCar(Car):
    nitro = 10
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        super().__init__(max_speed, acceleration, tyre_friction, color=None)
        
    def sound_horn(self):
        if self._is_engine_stared == True:
            print('Peep Peep\nBeep Beep')
        else:
            print('Start the engine to sound_horn')

    
    
        


# car = Car(max_speed=250, acceleration=10, tyre_friction=3, color="Red")
# truck = Truck(max_speed=250, acceleration=10, tyre_friction=3, max_cargo_weight=100, color="Red")
racecar = RaceCar(max_speed=250, acceleration=50, tyre_friction=30, color="Red")
# racecar = RaceCar(color="Red", max_speed=250, acceleration=50, tyre_friction=30)



# sound_horn_when_car_engine_is_started: failed
racecar.start_engine()
racecar.sound_horn()



# print(car.acceleration)
# print(car.tyre_friction)
# print(car.max_speed)
# print(car.color)

# print(car.is_engine_stared)
# car.start_engine()
# print(car.is_engine_stared)

# print(car.current_speed)

# car.start_engine()  
# car.accelerate()  
# print(car.current_speed)
# car.accelerate()
# print(car.current_speed)

# car.accelerate()

# car.start_engine()  
# car.accelerate()
# print(car.current_speed)
# car.apply_brakes()  
# print(car.current_speed)

# car.start_engine()  
# car.sound_horn()

# car.sound_horn()

# car.start_engine()  
# print(car.is_engine_stared)
# car.stop_engine()  
# print(car.is_engine_stared)

# car.current_speed
# car.start_engine()
# print(car.current_speed)
# car.current_speed = 10

# truck.load(50)  
# truck.load(100)
# truck.load(-100)

# truck.start_engine()
# truck.accelerate()
# truck.load(50)

# truck.start_engine()
# truck.sound_horn()

# racecar.start_engine()  
# print(racecar.current_speed)
# racecar.accelerate()  
# print(racecar.current_speed)
# racecar.accelerate()  
# racecar.accelerate()
# print(racecar.current_speed)

# racecar.apply_brakes()
# print(racecar.current_speed)

# print(racecar.nitro)

# racecar.accelerate()
# print(racecar.current_speed)
# print(racecar.nitro)
# car.sound_horn()