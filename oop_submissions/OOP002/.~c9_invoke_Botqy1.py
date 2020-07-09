class Car:
    
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.current_speed = 0
    
    def start_engine(self):
        if self.acceleration > 0:
            is_engine_stared = True
            return is_engine_stared
    
    def accelerate(self):
        self.current_speed += self.acceleration
        return self.current_speed
    
    def apply_brakes(self):
        self.current_speed -= self.tyre_friction
        return self.current_speed
        
    def sound_horn(self):
        return 'Start the engine to sound_horn'
        
    def stop_engine()


car = Car("Red", 250, 10, 3)

print(car.acceleration)
print(car.tyre_friction)
print(car.max_speed)
print(car.color)
print(car.start_engine())
print(car.accelerate())
# print(car.current_speed)
print(car.apply_brakes())
print(car.sound_horn())






'''
car = Car(max_speed=250, acceleration=10, tyre_friction=3)  
>>> car.start_engine()  
>>> car.accelerate()  
>>> car.current_speed  
10  
>>> car.accelerate()  
>>> car.current_speed  
20
...
...
...
>>> car.current_speed
250
>>> car.accelerate()  
>>> car.current_speed
250
'''




'''
from car import Car  
>>> car = Car(max_speed=250, acceleration=10, tyre_friction=3)  
>>> car.start_engine()  
>>> car.is_engine_stared
True
'''








'''
from car import Car  
>>> car = Car(color="Red", max_speed=250, acceleration=10, tyre_friction=3)  
>>> car.acceleration  
10  
>>> car.tyre_friction  
3  
>>> car.max_speed  
250  
>>> car.color  
Red  
'''