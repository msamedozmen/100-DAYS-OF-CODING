
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
MORSE_REVERSE_CODE_DICT = {value:key for (key,value) in MORSE_CODE_DICT.items()}

sentence = input("What senctence u want to decode ?").upper()

if " " in sentence:
    new_sentence = sentence.replace(" ","")
else:
    new_sentence = sentence
my_letters= set(new_sentence)

def decode(replaced_sentence,my_letters):
    check_letters=my_letters
    for i in check_letters:
        replaced_sentence = replaced_sentence.replace(i,f"{MORSE_CODE_DICT[i]} ")
        print(replaced_sentence)
    return replaced_sentence

result= decode(sentence,my_letters)

print(result)

new_result = result.split(" ")
x=result
for i in new_result:
    print(i)
    if i =="":
        x = x
        print(x)
    else:
           
        x = x.replace(f"{i} ",f"{MORSE_REVERSE_CODE_DICT[i]}")

print(x)