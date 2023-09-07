# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

#Looping through dictionaries:
# for (key, value) in student_dict.items():
    #Access key and value
    # pass

import pandas as pd





data = pd.read_csv("nato_phonetic_alphabet.csv")


# student_data_frame = pandas.DataFrame(student_dict)
# print(letter_dict)
# print(code_dict)
final_list ={row.letter: row.code for (index,row) in data.iterrows()}

print(final_list)


ask_user_name = input("What is Your Name: ").upper()

final_code = [final_list[letterss] for letterss in ask_user_name]

for i in range(len(ask_user_name)):
    words =final_list[ask_user_name[i]]
    print(words)
print(final_code)
# print(letter_list)
#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

