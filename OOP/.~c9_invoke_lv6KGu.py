class device:
    
    def __init__(self,brand_name,cost,screen_size,ram,rom):
        self.brand_name = brand_name 
        self.cost = cost
        self.screen_size = screen_size 
        self.ram =  ram
        self.rom = rom
    
    def laptop(self):
        pass

    def mobile(self,slots_no):
        no_of_sim_slots = slots_no
        return  no_of_sim_slots
        
        
mobile_obj = device('realme',8000,'576x736',3,32)
laptop_obj = device('Apple',100000,'1920x1080',8,1000)



# print(mobile_obj)
# print(laptop_obj)
# print(mobile_obj.ram)
# print(laptop_obj.ram)
# print(mobile_obj.rom)
# print(laptop_obj.rom)
# print(mobile_obj.mobile(2))
print(mobile_obj)
