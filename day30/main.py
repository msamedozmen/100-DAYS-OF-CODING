

import pandas as pd





data = pd.read_csv("nato_phonetic_alphabet.csv")

final_list ={row.letter: row.code for (index,row) in data.iterrows()}

# First Way
is_true = True
while is_true:
    
    ask_user_name = input("What is Your Name: ").upper()

    try :
        final_code = [final_list[i] for i in ask_user_name]
    except KeyError:
        print("Please, only letters in alphabet")
    else:
        print(final_code)
        is_true = False


#Second Way 

# def phonetic():
#     ask_user_name = input("What is Your Name: ").upper()

#     try :
#         final_code = [final_list[i] for i in ask_user_name]
#     except KeyError:
#         print("Please, only letters in alphabet")
#         phonetic()
#     else:    
#         print(final_code)
        
# phonetic()