import pandas as pd
import csv
with open('cafe-data.csv', newline='') as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)


print(list_of_rows)