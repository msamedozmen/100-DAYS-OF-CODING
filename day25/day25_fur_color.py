import pandas as pd

data = pd.read_csv("day25\y018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"])

gray_fun_color = len(data[data["Primary Fur Color"] =="Gray"])
red_fun_color = len(data[data["Primary Fur Color"] =="Cinnamon"])
black_fun_color = len(data[data["Primary Fur Color"] =="Black"])

new_csv = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count" : [gray_fun_color,red_fun_color,black_fun_color]
    
    
}

print(len(data[data["Primary Fur Color"] =="Gray"]))

new_data = pd.DataFrame(new_csv)
new_data.to_csv("a.csv")
print(new_data)