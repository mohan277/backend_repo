"""score = 100
print(score)#100 integer
score = 99.9
print(score)#99.9 float

course = "python programming"
print(course)#python programming

course = "python programming"

print(len(course))#18
print(course[0])#P
print(course[-1])#g
print(course[-2])#n
print(course[0:3])#Pyt
print(course[:3])#Pyt
print(course[0:])#Python programming
print(course[:])#Python programming
print(course[-18])#P
print(course[0:(len(course)-10)])#Python p
print(course[:len(course)])#Python programming
#print(course[-19])#Error : string index out of range


is_published = True
print(is_published)#True
is_published = False
print(is_published)#False


print("Python \ programming")

"""
#j=k
"""
for i in range( 1 , 2*k-1 , 1 ):
    if i>=k:
      print(" "*(k-i),"*"*(2*i-1))
    else:
      print(" "*(i-k-j),"*"*(2*i-1))
#for i in range( k ,0 , -1 ):
#    print(" "*(k-i),"*"*(2*i-1))
"""
"""
cmd = ""
while cmd.lower() != "mohan":
  cmd = input(">")
  print("krish:",cmd)
  

def multiply(*numbers):
  total = 1
  for number in numbers:
    total *= number
  return total

print(multiply (1,2,3,4,5))
"""

def increment(number, by=1):
  return number + by

print(increment(2,5))