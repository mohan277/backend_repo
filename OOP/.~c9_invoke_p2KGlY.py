class  Bike:
    def  __init__(self, model_name, acceleration):
        self.model_name = model_name
        self.acceleration = acceleration
        self.current_speed =  0
        self.color =  "black"

    def accelerate(self):
        self.current_speed += self.acceleration


    return bike_object
    pass
	
def get_bike_object_color(bike_object):
    return 

def get_bike_object_current_speed(bike_object):
	return  "To fill get_bike_object_current_speed code" # Change this

def change_bike_color(bike_object, new_color):
	return  "To fill change_bike_color code" # Change this

def increase_bike_speed(bike_object):
	return  "To fill increase_bike_speed code" # Change this


if  __name__  ==  '__main__':
    bike_object =  Bike('Yamaha',10)
    print(bike_object)
    print(get_bike_object_color(bike_object))
    print(get_bike_object_current_speed(bike_object))
    print(change_bike_color(bike_object, "red"))
    print(increase_bike_speed(bike_object))
    print(get_bike_object_current_speed(bike_object))
    
    