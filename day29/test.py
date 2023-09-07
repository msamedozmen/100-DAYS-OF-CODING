import string
import random

letters_lower = list(string.ascii_lowercase)
letters_upper = list(string.ascii_uppercase)
numbers = list(string.digits)
punctuation = list(string.punctuation)

all_keys = letters_lower+letters_upper+numbers+punctuation

generated_pass =random.choices(all_keys,k=(random.randint(8,12)))

final_pass = ""
for i in generated_pass:
    final_pass += i
print(final_pass)