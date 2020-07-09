class device:
    
    def __init__(self,brand_name,cost,screen_size,ram,rom):
        self.brand_name = brand_name 
        self.cost = cost
        self.screen_size = screen_size 
        self.ram =  ram
        self.rom = rom
    
class laptop(device):
    def __init__(self,brand_name,cost,screen_size,ram,rom,no_of_cells):
        super().__init__(brand_name,cost,screen_size,ram,rom)
        self.no_of_cells = no_of_cells
        
class mobile(device):
    def __init__(self,brand_name,cost,screen_size,ram,rom,no_of_slots):
        super().__init__(brand_name,cost,screen_size,ram,rom)
        self.no_of_slots = no_of_slots
        
        
        
mobile_obj = mobile('realme',8000,'576x736',3,32,2)
laptop_obj = laptop('Apple',100000,'1920x1080',8,1000,8)



# print(mobile_obj)
# print(laptop_obj)
# print(mobile_obj.ram)
# print(laptop_obj.ram)
# print(mobile_obj.rom)
# print(laptop_obj.rom)
print(mobile_obj.brand_name)
print(laptop_obj.brand_name)
print(laptop_obj.no_of_cells)