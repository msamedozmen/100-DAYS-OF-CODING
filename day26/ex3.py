
import pandas

with open("file1.txt") as d1:
    data1=d1.readlines()
    # data1.strip()
with open("file2.txt") as d2:
    
    data2=d2.readlines()
    # data2.strip()

result =[int(n) for n in data1 if n in data2]
# Write your code above 👆

print(result)


