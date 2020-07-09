# import datetime


# print(datetime.datetime.today())
# print(datetime.datetime.today().strftime("%Y"))
# print(datetime.datetime.today().strftime("%B"))
# print(datetime.datetime.today().strftime("%W"))
# print(datetime.datetime.today().strftime("%w"))
# print(datetime.datetime.today().strftime("%j"))
# print(datetime.datetime.today().strftime("%d"))
# print(datetime.datetime.today().strftime("%A"))

# _________Isleap_____________

# import calendar
# year = int(input())
# print(calendar.isleap(year))

# import datetime
# x = input()
# f = "%b %d %Y %I:%M%p"
# y = datetime.datetime.strptime(x,f)
# print(y)

# import datetime
# print(datetime.datetime.now().date())
# print(datetime.datetime.now().time())


# from datetime import date, timedelta
# t1 = date.today()
# t2 = timedelta(days=5)
# print(t1-t2)   
# print(t1+t2)    

# import datetime
# print(datetime.datetime.fromtimestamp(int("1284105682")).strftime("%Y-%m-%d %H:%M:%S"))

# from datetime import date
# from datetime import datetime
# d = date.today()
# print(datetime.combine(d, datetime.min.time()))

# import datetime

# from datetime import timedelta,time
# t1 = datetime.datetime.now()
# print(t1)
# t2 = timedelta(seconds=5)
# print((t1+t2).time())

# from datetime import date
# import datetime
# x = input()
# f = "%Y %m %d"
# print(datetime.datetime.strptime(x,f).strftime("%j"))

# import time
# import datetime

# print(datetime.datetime.today().total_milliseconds())

# import datetime
# print(datetime.datetime.now().strftime("%W"))
