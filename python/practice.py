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
# nums1 = {1,2,3,4,5}
# print(nums1.issubset(nums))
# print(nums1 < nums)

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


print((1, 2, 5) >= (1, 2, 4))
print([1, 2, 3]              < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4)           < (1, 2, 4))
print((1, 2)                 < (1, 2, -1))
print((1, 2, 3)             == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))