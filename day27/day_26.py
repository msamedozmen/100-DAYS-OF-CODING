student = {
    "student":["samet","emre","aahmet"],
    "score":[5,6,7]
}


import pandas as pd


data =pd.DataFrame(student)


# print(data)

# for (key,value) in data.items():
    #print(key)
    # print(value)
    
for (key,value) in data.iterrows():
    if value.student == "samet":
        print(value)
    