    

# data_list=[]
# with open("day25\weather_data.csv",mode ="r") as file:
#     lines =file.readlines()
#     print(lines)

# for line in lines:
#     data_list.append(line)
        

# print(data_list)

# import csv 

# with open("day25\weather_data.csv",) as file:
#     datas = csv.reader(file)
#     tempetures = []
#     for data in datas:
#         if data[1] != "temp":
#             tempetures.append(int(data[1]))
    
# print(tempetures)

import pandas

file =pandas.read_csv("weather_data.csv")
#print(file)
print(file["temp"])

average_temp = file["temp"].to_list()
sum=sum(average_temp)/len(average_temp)
print(sum)

print(file["temp"].max())

print(file[file.temp == 24])