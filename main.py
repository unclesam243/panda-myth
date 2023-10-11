#import csv
#
# #with open("weather_data.csv") as file:
#   data = csv.reader(file)
#   temperature = []
#   for row in data:
#       if row[1] != 'temp':
#           temperature.append(int(row[1]))

#   print(temperature)
import pandas

#data = pandas.read_csv("weather_data.csv")
#print(data[data.temp == data["temp"].max()]) #OR
#print(data[data.temp == data.temp.max()])

#Creating a new dataFrame from scratch
#data_dict = {
#    "students": ["Jason", "James", "Amber"],
#    "scores": [12, 50, 21]
#}
#
#data = pandas.DataFrame(data_dict)
#
#data.to_csv("student_scores.csv")


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_sq = len(data[data["Primary Fur Color"] == 'Gray'])
black_sq = len(data[data["Primary Fur Color"] == 'Black'])
red_sq = len(data[data["Primary Fur Color"] == 'Cinnamon'])


total_squirrel_data ={
    "Primary Fur Color": ["Grey", "Black", "Red"],
    "Count": [grey_sq, black_sq, red_sq]
}

data = pandas.DataFrame(total_squirrel_data)
data.to_csv("total_squirrels.csv")