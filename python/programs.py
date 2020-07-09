# name = input()
# count = int(input())

# for i in range(count):
#     func = input()
#     str = func.split(" ")
#     if str[0]=="find":
#         print(name.find(str[1]))
#     elif str[0]=="count":
#         print(name.count(str[1]))
#     elif str[0]=="substring":
#         comma = str[1].split(",")
#         print(name[2:3])
#     elif str[0]=="startswith":
#         print(name.startswith(str[1]))
#     elif str[0]=="remove":
#         re_place = name.replace(str[1],"")
#         print(re_place)

#myTuple = ("John", "Peter", "Vicky")

# for i in range(1):
#     x = "#".join(name)
#     print(x)

#num = [1, 2, 3, 4, 5]
# num.remove()
# print(num)
# num.append(6)
# print(num)
# num.extend(6)
# print(num)

# name = "mohan"
# print(name.center(20,"*"))
# name = "MohAn"
# print(name.casefold())

# name = "mohan"
# print(name.capitalize())

# name = "mohan"
# print(name.center(20,"*"))

#name = "The sum of 1 + 2 is {0}"
#mohan = "hello"
#print(name.format(1 + 2))

# name = "The sum of"
# print(name.upper())

# name = "cricket"
# print(name.count("c",0,3))

# name = "cricket"
# print(name.endswith(("t","c")))

# name = "9"
# print(name.isdigit())
# print(name.isdecimal())

# i = 6
# num = [1, 2, 3, 4, 5]
# num.pop()
# print(num)
# num.append(int(input()))
# print(num)


#for i in range():
# result = []
# while True:
#     str1 = input()
#     sp_lit = str1.split(" ",1)
#     try:
#         if sp_lit[0] == "PUSH":
#             result.insert(0,sp_lit[1])
#         elif sp_lit[0] == "POP":
#             if len(result) == 0:
#                 print("Emty Stack!")
#             else:
#                 result.pop(0)
#         elif sp_lit[0] == "PRINT":
#             for i in result:
#                 print(i)
#         elif sp_lit[0] == "EXIT":
#             break
#     except:
#         continue

# num = 1000
# number = str(num)
# for i in number:
#     print(i)

# num = int(input())
# x=num-1
# for i in range (num-1):
#     print(f'{"2"*i}*{"1"*(2*x-1)}*{"3"*i}')
#     x-=1
# print(f'{"2"*(num-1)}*{"3"*(num-1)}')
# x=1
# for i in range (num-1,0,-1):
#     print(f'{"2"*(i-1)}*{"4"*(2*x-1)}*{"3"*(i-1)}')
#     x+=1

# name = "aaabbccaadddeee"
# x=name[0]
# for i in range(len(name)-1):
#     if name[i] != name[i+1]:
#         print(name[i],end="")
# print(name[i],end="")

# from collections import Counter
# str1 = input()
# d = Counter(str1)
# print(d)
# for k,v in d.items():
#     if v>1:
#         print(k)

# lis = []
# name = input()
# for i in name:
#     cnt = name.count(i)
#     if cnt>1 and i not in lis:
#         lis.insert(0,i)
#         print(i)

# lis = []
# num = input()
# numbers = num.split(",")
# for i in numbers:
#     cnt = numbers.count(i)
#     if (len(numbers)//2) < cnt and i not in lis:
#         lis.insert(0,i)
#         print(i)
# #print(numbers)

# matrix1 = []
# matrix2 = []
# indexes = input()
# indexes1 = indexes.split(",")
# m = int(indexes1[0])
# n = int(indexes1[1])
# for i in range(m):
#     matrix1.append(input().split(","))
#     print(matrix1)
# matrix2=[[row[i] for row in matrix1] for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         if(j!=m-1):
#             print(matrix1[i][j],end = ',')
#         else:
#             print(matrix1[i][j])

#squares = list(map(lambda x: x**2, range(10)))
# y = [1,2,3,4,5]
# for i in range(len(y)):
#     squares = [y for x in range(10)]
#     print(i)

# list1 = input().split(",")
# list2 = input().split(",")
# cnt = 0
# for i in list2:
#     if i in list1:
#         cnt+=1
# print(cnt == len(list2))
# print(list1)
# print(list2)

# a = set(input().split(","))
# b = set(input().split(","))
# print(b <= set(a))


# import math

# print(math.ceil(4.0))
# print(math.floor(4.0))
# print(math.ceil(3.3))
# print(math.floor(3.3))
# print(math.ceil(3.4))
# print(math.floor(3.4))
# print(math.ceil(3.5))
# print(math.floor(3.5))

# names = ['mohana','krishna','senam']
# y = ""
# for i in names:
#     y  += i.capitalize()+" "
# print(y)


# name = "mohana krishna"
# print(name[::2])#2 is for step

# s = "mohana krishna"
# print(s.index('a',6,))

# name = [1,2,3]
# for i in name:
#     print(i,end = "")

# a = [ None ] * 3
# print(a)

# for i in range(3):
#     a[i] = [ None ] * 2
# print(a)
# w,h = 2,3
# a = [ [ None ] * w for i in range (h) ]


# a[1][0]= 5
# print(a)

# num = ['100','dfgh']
# del num[:1]
# print(num)

# s= 'mohana krishna'
# print(s.partition('o'))

# nums = {1,2,3,4,5,6}
# nums1 = {1,2,3,4,5,6}
# print(nums1.issubset(nums))
# print(nums1 < nums)

# nums = {1,2,3,4,5,6}
# nums1 = {1,2,3,7,8,9}
# print(nums1.symmetric_difference(nums))
# print(nums1 ^ nums)

# name = "mohana"
# print(list(name.partition("a")))

# name = "mohana sanem"
# print(name.rpartition("a"))


# name = "mohana"
# print(10)
# print(name.rjust(20))

# nums1 = {100,1,2,3,4,31,32}
# nums2 = {100,11,12,13,14,21,22}
# nums3 = {100,21,22,23,1,2}
# nums4 = {100,31,32,33,34,12,13}
# s = nums1 - nums2 
# print(s)
# b=s- nums3
# print(b)
# c=b- nums4
# print(c)

# num = [1,2,3,4,31,32]
# num.reverse()
# print(num)



# nums = {1,2,3,4,5,6}
# nums1 = {8,9}
# nums2 = {11,12,13}
# #print(nums.update(nums1))
# print(nums)
# print(nums1)
# print(nums2)
# nums &= nums1 & nums2
# print(nums)
# print(nums1)
# print(nums2)

# nums = {1,2,3}
# nums.remove(3)
# print(nums)

# nums = {1,2,3}
# nums.add(6)
# print(nums)

# nums_list = [1,2,3]
# nums = {1,2,3}
# print(nums.remove(6))
# print(nums_list.pop())

# names = {'one':1,'two':2,'three':3}
# print(list(names),len(names))
# print('one' in names)
# print(names['one'])
# k = names.copy()
# k['one']=4
# print(k)
# print(names)
# print(names.values())
# print(names.keys())
# print(names['two'])
# print(names.get('one'))
# print(names.setdefault('nine'))

# names = {'one':1,'two':2,'three':3}
# x_keys = names.keys()
# y_values = names.values()
# print(*x_keys)
# print(*y_values)

# from collections import Counter

# names = ['two','three','one','three' ,'two','three']
# z = Counter(names)
# print(z)
# for i,j in z.items():
#     print(i,j)



# x_keys = names.keys()
# y_values = names.values()
# print(*x_keys)
# print(*y_values)



# for i in range(5):
#     print(i)
#     break
# else:
#     print('mohan')

# import random
# value = random.random()
# print(value)

# import random
# value = random.uniform(1,10)
# print(value)

# import random
# value = random.randint(1,6)
# print(value)

# import random
# greetings = ['hi', 'hello','howdy','vanakam']
# value = random.choice(greetings)
# print(value + ', mohan')

# num = [1,2,3,4,5,6,7]
# print(num.index(1))
# print(num)

# d = {}
# num = int(input())
# for i in range(num):
#     names = input().split(" ")
#     d.update([names])
# print(d)

# names = {'jack': 4098, 'sape': 4139, 'guido': 4127}
# k = sorted(names)
# print(sorted(names))
# print(k)

# names = [1,3,5,7,345,39,56,8,9]
# for i, v in enumerate(names,start = 10):
#     print(i, v)


# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)



# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('What is your {0}?  It is {1}.'.format(q, a))


# print((1, 2, 5) >= (1, 2, 4))
# print([1, 2, 3]              < [1, 2, 4])
# print('ABC' < 'C' < 'Pascal' < 'Python')
# print((1, 2, 3, 4)           < (1, 2, 4))
# print((1, 2)                 < (1, 2, -1))
# print((1, 2, 3)             == (1.0, 2.0, 3.0))
# print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))


# single = 'mohan',
# print(len(single))

#names = {'jack':['sdfghjk',4098,455,765,7654,7654], 'sape': 4139, 'guido': 4127}
#print(names)

# import os
# print(os.listdir())

# name = " mohana krishna "
# print(name.lstrip())

# print(name.rstrip())

# print(name.strip())


# Social infra
# https://docs.google.com/document/d/1vPTEUmdJ0-JiWME7gr_ttg7vEnHdiOJve8C2-k3gs1M/mobilebasic


# PPT
# https://docs.google.com/presentation/d/1B5gYEkBllyK8fPWUicwNyWv7S1cRif0ozH1D6-uNsQA/mobilepresent?slide=id.g6470b2541d_360_41

# import textwrap
# name = 'mohan'
# print(textwrap.wrap(name,width=70))

# import textwrap
# name1 = 'mohana       krishna'
# print(textwrap.shorten(name1,14))
# name = 'mohana krishna'
# print(textwrap.wrap(name,2))
# print(textwrap.fill(name,2))
# print(len(name))
# print(textwrap.shorten(name,1,placeholder = ""))
# print(textwrap.shorten(name,14))
# print(textwrap.shorten(name,5))

# import textwrap
# name = '''\
# my name \n\n\n
#  is mohan
# '''
# print(repr(name))
# print(repr(textwrap.dedent(name)))
# print(textwrap.indent(name,"# "))
# print(textwrap.indent(name,"# ",lambda line : True))


#____________datetime___________

# import datetime
# d = datetime.date(2019,9,12)
# print(d)

# import datetime
# tday = datetime.date.today()
# print(tday)
# print(tday.year)
# print(tday.month)
# print(tday.day)
# print(tday.weekday())
# print(tday.isoweekday())

# import datetime
# tday = datetime.date.today()
# tdelta = datetime.timedelta(days=30)
# print(tday + tdelta)
# print(tday - tdelta)


# import datetime
# tday = datetime.date.today()
# tdelta = datetime.timedelta(days=30)

# bday = datetime.date(2020,12,9)
# till_day = bday - tday
# print(till_day)
# print(till_day.days)
# print(till_day.total_seconds())

# import datetime
# t = datetime.time(9,9,9,99999)
# print(t.hour)
# print(t.second)
# print(t.microsecond)

# import datetime
# dt = datetime.datetime(2020,1,11,9,9,9,99999)
# print(dt)
# print(dt.date())
# print(dt.time())
# print(dt.year)
# print(dt.month)
# print(dt.day)
# print(dt.hour)
# print(dt.second)
# print(dt.microsecond)

# import datetime
# dt = datetime.datetime(2020,1,11,9,9,9,99999)

# a = [1,2,3]
# b = [4,5,6]
# a[0] = b
# b[0] = 10
# print(a)




# name = "mohana"
# print(len(name))
# print(name[:4:-1])

# import math
# n = 1.9
# print(math.floor(n))
# print(math.ceil(n)) 
# print(n)


# n= 11
# if 10<n<20:
#     print("mohana")
# else:
#     print("krish")
    
# random function for integers
# import random
# value = random.random()
# value = random.uniform(1,10)
# n = [1,2,3,4,5]
# names = ["hi","hello","sai"]
# value = random.choice(names)
# print(value + " banda badri")
# value = random.randrange(10)
# value = random.randrange(5,10)
# value = random.randrange(3,10,2)
# value = random.randint(1,10)
# value = random.shuffle(n)
# value = random.sample(1,10)
# print(value)



# name  = "mohana"
# print(name.rjust(7))
# print(name.ljust(10))

# print(divmod(4,2))

# import math
# n = 10.9
# print(math.trunc(n))
# print(round(n-math.trunc(n),4))
# print(round(n-math.trunc(n),4))

# print(round(4.6))

# s1 = "mohanakrishna!"
# s2 = "ana"
# lis = []
# for i in range(len(s1)):
#     if i < (len(s1)-(len(s2))):
#         lis.append(s1[i:i+len(s2)])
# print(lis)
# print()

# for i in range(len(s1)//len(s2)):
#     lis.append(s1[i:i+len(s2)])
# print(lis)


# ______alpha rangoli_______
# _____metho-1______

# n = 5
# for i in range(n):
#     for l in range((n+(n-i))-i-2):
#         print(end="-")
#     for j in range(96+n,96+n-i,-1):
#         print(chr(j),end="-")
#     for k in range(96+n-i,96+n+1):
#         if k == 96+n:
#             print(chr(k),end="")
#         else:
#             print(chr(k),end="-")
#     for m in range((n+(n-i))-i-2):
#         print(end="-")
#     print()
# for i in range(1,n):
#     for l in range(i+(i*1)):
#         print(end="-")
#     for j in range(96+n,97+i,-1):
#         print(chr(j),end="-")
#     for k in range(96+i+1,96+n+1):
#         if k == 96+n:
#             print(chr(k),end="")
#         else:
#             print(chr(k),end="-")
#     for l in range(i+(i*1)):
#         print(end="-")
#     print()

# ________method-2_________

# import string
# x = string.ascii_lowercase
# n = 5
# l = []
# for i in range(n):
#     s = "-".join(x[i:n])
#     l.append((s[::-1]+s[1:]).center(4*n-3,"-"))
# print('\n'.join(l[:0:-1]+l))

# ______itertools______

# import itertools
# n = ['a','b','c']
# print(*itertools.combinations(n,2))
# print(*itertools.permutations(n,2))
# print(*itertools.combinations_with_replacement(n,2))


# __________permutations__________
# num = [1,2,3,4,5,6]
# n = ['a','s','e','w']
# [print() for i in n]


# _________datetime_______

# import datetime
# print(datetime.datetime.today())
# print(datetime.datetime.today().strftime("%Y"))
# print(datetime.datetime.today().strftime("%B"))
# print(datetime.datetime.today().strftime("%W"))
# print(datetime.datetime.today().strftime("%w"))
# print(datetime.datetime.today().strftime("%j"))
# print(datetime.datetime.today().strftime("%d"))
# print(datetime.datetime.today().strftime("%A"))

# dict = {'m':1 ,'n':2}
# print(dict['m']

# s = '5.67'
# s = 'mohana'
# s = [1,2,3,4,5,'a','b','C','D']
# a = "".join(sorted(s))
# a = "".join(min(s))
# print(min(s))
# print(max(s))
# print(s.center(20,"#"))
# print(int(float(s)))
# print(s.islower())
# s = 'm o h a n a'
# x = s.split(maxsplit=4)
# print(x)

# print(s.startswith("mah"))


# s = 'abcdcdc'
# x = 'cdc'
# c = 0
# for i in range(len(s)):
#     if s[i:i+len(x)].startswith(x):
#         c += 1
# print(c)

# print(s.partition("b"))

s = 'mohana krishna'
# print(s.rfind("x"))
# print(s.index("x"))
# print(s.rindex("a"))
# print(s.title())


# names = ['a','b','c']
# num = [1,2,3]
# x = dict.fromkeys(names)
# d = {'a':1,'b':2,'c':3}
# print(d['a'])
# print(list(d))
# print(d.keys())
# print(list(d.keys()))
# print(*list(d.keys()))
# print(d.values())
# print(list(d.values()))
# print(*list(d.values()))

# d.update(mohan=10)
# print(d)



# d = {1: "one", 2: "three"}
# d1 = {2: "two"}

# updates the value of key 2
# d.update(d1)
# print(d)

# d1 = {3: "three"}

# adds element with key 3
# d.update(d1)
# print(d)

# d = {'a':1,'c':1,'b':2,'e':1,'d':6}
# x = (sorted(d.values()))
# print(dict(x))
# # print(d)

# matrix = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# x = [[row[i] for row in matrix] for i in range(4)]
# print(x)

# for i in range(4):
#     for j in matrix:
#         print(j[i])
#     print()


# pattern = r'^[^aeiouAEIOU][aeiouAEIOU]{2,}[^aeiouAEIOU]$'

# from collections import Counter

# names = ['c','b','c','b','c','a','b','c']
# print(Counter(names))
# print(Counter(names).most_common())



# import textwrap
s = 'DescriptionPython is an interpreted, high-level, general-purpose programming language.'
# s  = 'This is a very very very very very long string'
# print(textwrap.wrap(s,18))
# print(textwrap.fill(s,18))

# import textwrap
# s = 'DescriptionPython'
# print(textwrap.wrap(s,3))


# names = ['c','b','c','b','c','a','b','c']
# num = [1,2,3]
# print(';'.join(num))
# print(';'.join(names))

# n = 'maaan'
# x = set(n)
# print(''.join(x))

# num = [1,2,3]
# m = list(map(int,num))
# print(n)
# print(m)
# import string
# x = string.ascii_lowercase
# x = string.ascii_lowercase
# print(x)


# import collections
# d = {'a':1,'c':1,'b':2,'e':1,'d':6}
# x = **d
# print(x)

# import collections 
  
# # Declaring namedtuple() 
# Student = collections.namedtuple('Student',['name','age','DOB']) 
  
# # Adding values 
# S = Student('Nandini','19','2541997') 
  
# # initializing iterable  
# li = ['Manjeet', '19', '411997' ] 
  
# # initializing dict 
# di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' }


#import collections 
  
# Declaring namedtuple() 
#Student = collections.namedtuple('Student',['name','age','DOB']) 
  
# Adding values 
#S = Student('Nandini','19','2541997') 
  
# initializing iterable  
#li = ['Manjeet', '19', '411997' ] 
  
# initializing dict 
#di = { 'name' : "Nikhil", 'age' : 19 , 'DOB' : '1391997' }

# import requests 
# from bs4 import BeautifulSoup 
  
# URL = "http://www.values.com/inspirational-quotes"
# r = requests.get(URL) 
  
# soup = BeautifulSoup(r.content, 'html5lib') 
# print(soup.prettify()) 


import os
# print(os.name)
# print(os.getcwd())
# To print absolute path on your system 
# print(os.path.abspath('.'))

# To print files and directories in the current directory 
# on your system 
# print(os.listdir('.'))
# for roots,dirs,files in os.walk(os.getcwd()):
#     print(roots,dirs,files,sep="\n")
# for i in range(3):
#     x = os.chdir()
#     print(os.getcwd())
# os.mkdir('krish3/krish4/krish5')
# os.makedirs('krish3/krish4/krish5')
# print(os.getcwd())
# os.rmdir('krish3/krish4/krish5')
# os.removedirs('krish1/krish2')
# os.rename('pora.py','practice.py')
# import csv
# rows = []
# fields = []
# #filename = 'csv_data.csv'
# with open ('csv_data.csv','r') as f:
#     cr = csv.reader(f)
#     #fields = csvreader.next()
# for i in cr:
#     rows.append(i)
# for i in rows:
#     print(i)

# import csv 
  
# # csv file name 
# filename = "csv_data.csv"
  
# # initializing the titles and rows list 
# fields = [] 
# rows = [] 
  
# # reading csv file 
# with open(filename, 'r') as csvfile: 
#     # creating a csv reader object 
#     csvreader = csv.reader(csvfile) 
    
#     #fields = csvreader.next() 
#     for row in csvreader: 
#         rows.append(row)
#     #print(rows[0])
#     # get total number of rows 
#     print("Total no. of rows: %d"%(csvreader.line_num)) 
  
# # printing the field names 
# print('Field names are:' + ', '.join(field for field in fields)) 
  
# #  printing first 5 rows 
# print('\nFirst 5 rows are:\n') 
# for row in rows[:5]: 
#     # parsing each column of a row 
#     for col in row: 
#         # print(col,end=",")
#         print('%20s'%col) 
#     print('\n') 
    
    
import os
# l =  [0,1,2,3,4,5].__iter__()
# value = l.next()
# for i in l:
#     print(i)
# iterator = [0, 1, 2, 3, 4, 5]
# value = iterator.csvreader.__next__()
# for v in iterator:
#     print (v)
# print (value)


    
# nums = [1,2,3,5,6,7]
# for i,j in enumerate(nums):
#     print(i,j)
    
    
    
    
    