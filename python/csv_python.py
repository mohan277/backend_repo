# import csv
# with open('csv_data.csv','r') as csv_file:
#     csv_reader = csv.reader(csv_file)
    
#     for line in csv_reader:
#         print(line[0],line[1],line[2],line[3])


names  = {'mohan':277,'krishna':2345}
print(names['mohan'])
names.popitem()
print(names)