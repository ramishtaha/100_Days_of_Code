# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()
#     print(data)
# import csv
#
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     flag = False
#     temperatures = []
#     for row in data:
#         if flag:
#             temperatures.append(int(row[1]))
#         flag = True
#     print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')
# print(data['temp'])

# data_dict = data.to_dict()
# # print(data_dict)
#
# data_list = data['temp'].to_list()
# print(sum(data_list)/len(data_list))
# print(data['temp'].mean())
# print(data['temp'].max())

# Get Data in Columns
# print(data.condition)

# Get Data in Rows

# print(data[data.day == "Monday"])

# Row of data with the Highest Temperature

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
#
# print(int(monday.temp) * 9 / 5 + 32)

# Create Dataframe from Scratch

# data_dict = {
#     'students': ["Amy", "James", "Angela"],\
#     'scores': [74, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# Save the Data to CSV

# data.to_csv("new_data.csv")


import pandas

squirrel_census_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
black_squirrels_count = len(squirrel_census_data[squirrel_census_data['Primary Fur Color'] == 'Black'])
grey_squirrels_count = len(squirrel_census_data[squirrel_census_data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrels_count = len(squirrel_census_data[squirrel_census_data['Primary Fur Color'] == 'Cinnamon'])

data_dict = {
    "Fur Color": ["Grey", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")


print(black_squirrels_count)
print(grey_squirrels_count)
print(cinnamon_squirrels_count)




















