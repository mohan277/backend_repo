class Employee:
    def __init__(self,first,second,hometown,age):
        self.first = first
        self.second = second
        self.email = first + '.' + second + '@' +'gmail.com'
        self.hometown = hometown
        self.age = age
    

    
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    
# class Robot:

#     Three_Laws = (
# """A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
# """A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
# """A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""
# )

    # def __init__(self, name, build_year):
    #     self.name = name
    #     self.build_year = build_year

    # other methods as usual    
    
# from robot_asimov import Robot
# for number, text in enumerate(Robot.Three_Laws):
#     print(str(number+1) + ":\n" + text) 

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# class C: 

#     counter = 0
    
#     def __init__(self): 
#         type(self).counter += 1

#     def __del__(self):
#         type(self).counter += 1
        
# if __name__ == "__main__":
#     x = C()
#     print("Number of instances: : " + str(C.counter))
#     y = C()
#     print("Number of instances: : " + str(C.counter))
#     del x
#     print("Number of instances: : " + str(C.counter))
#     del y
#     print("Number of instances: : " + str(C.counter))




# class Robot:
#     __counter = 0
    
#     def __init__(self):
#         type(self).__counter += 1
        
#     def RobotInstances(self):
#         return Robot.__counter
        

# if __name__ == "__main__":
#     x = Robot()
#     print(x.RobotInstances())
#     y = Robot()
#     print(x.RobotInstances())


# class Robot:
#     __counter = 0
    
#     def __init__(self):
#         type(self).__counter += 1
        
#     @staticmethod
#     def RobotInstances():
#         return Robot.__counter
        

# if __name__ == "__main__":
#     print(Robot.RobotInstances())
#     x = Robot()
#     print(x.RobotInstances())
#     y = Robot()
#     print(x.RobotInstances())
#     print(Robot.RobotInstances())

# class fraction(object):

#     def __init__(self, n, d):
#         self.numerator, self.denominator = fraction.reduce(n, d)
        

#     @staticmethod
#     def gcd(a,b):
#         while b != 0:
#             a, b = b, a%b
#         return a

#     @classmethod
#     def reduce(cls, n1, n2):
#         g = cls.gcd(n1, n2)
#         return (n1 // g, n2 // g)

#     def __str__(self):
#         return str(self.numerator)+'/'+str(self.denominator)
# x = fraction(8,24)
# print(x)

class Pet:
    _class_info = "pet animals"

    def about(self):
        print("This class is about " + self._class_info + "!")   
    

class Dog(Pet):
    _class_info = "man's best friends"

class Cat(Pet):
    _class_info = "all kinds of cats"

p = Pet()
p.about()
d = Dog()
d.about()
c = Cat()
c.about()