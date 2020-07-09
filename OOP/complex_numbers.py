import math
class ComplexNumber:
    def __init__(self, real_part = 0, imaginary_part = 0):
        self.real_part = real_part
        self.imaginary_part = imaginary_part
        if type(self.real_part) == str and type(self.imaginary_part) == str:
            raise ValueError('Invalid value for real and imaginary part')
        elif type(self.real_part) == str :
            raise ValueError('Invalid value for real part')
        elif type(self.imaginary_part) == str :
            raise ValueError('Invalid value for imaginary part')
    
    def conjugate(self):
        return ComplexNumber(self.real_part,-1 * self.imaginary_part)
        
    def __str__(self):
        if self.imaginary_part < 0 :
            return f'{self.real_part}{self.imaginary_part}i'
        else:
            return f'{self.real_part}+{self.imaginary_part}i'
    
    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part,self.imaginary_part + other.imaginary_part)
    
    def __sub__(self, other):
        return ComplexNumber(self.real_part - other.real_part,self.imaginary_part - other.imaginary_part)
            
    def __mul__(self, other):
        return ComplexNumber(((self.real_part * other.real_part)+(-1 * (self.imaginary_part * other.imaginary_part))), ((self.real_part * other.imaginary_part)+(other.real_part * self.imaginary_part)))
            
    def __truediv__(self, other):
        numerator_real = (self.real_part * other.real_part)+(-1 * (self.imaginary_part * (-1 * other.imaginary_part)))
        numerator_imaginary = (self.real_part * (-1 * other.imaginary_part))+(other.real_part * self.imaginary_part)
        denominator = pow(other.real_part,2) + (pow(other.imaginary_part,2))
        return ComplexNumber(round(numerator_real/denominator,3),round(numerator_imaginary/denominator,3))
        
    def __abs__(self):
        return round(math.sqrt(self.real_part**2 + self.imaginary_part**2),3)
            
    def __eq__(self,other):
        return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part
        
one_plus_two_i = ComplexNumber(1,2)
three_plus_four_i = ComplexNumber(2,6)
# absolute_value = abs(one_plus_two_i)
# addition = one_plus_two_i + three_plus_four_i
# subtraction = one_plus_two_i - three_plus_four_i
# multiplication = one_plus_two_i * three_plus_four_i
# division = one_plus_two_i / three_plus_four_i
# print(one_plus_two_i.real_part)
# print(one_plus_two_i.imaginary_part)
# print(absolute_value)
# print(one_plus_two_i.conjugate())
# print(addition)
# print(subtraction)
# print(multiplication)
# print(division)
# print(ComplexNumber(1,2) == ComplexNumber(1,2))








