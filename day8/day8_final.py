
from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode_word(text,shift):
    
    text_list =list()
    blankless_list=[]
    space_positions =list()
    for letter in text:
        text_list.append(letter)
    
    
    for i in range(0,len(text_list)):
        if text_list[i] == " ":
            space_position = text_list.index(" ")
            space_positions.append(i)

    for blank in text_list:
        if blank.strip():
            blankless_list.append(blank)
    text_list=blankless_list
        
    ntext=""
    for i in range(0,len(text_list)) :
        ntext = ntext + text_list[i]
        
    new_text = list()
    
    for letter in ntext:
        position= alphabet.index(letter)
        position=int(position)
        new_position = position+shift
        if new_position < len(alphabet):
            new_letter = alphabet[new_position] 
            new_text.append(new_letter)
        else:    
            while new_position>=len(alphabet):

                new_position = new_position - len(alphabet)
                updated_position = new_position

            if updated_position <len(alphabet):
                new_letter = alphabet[updated_position] 
                new_text.append(new_letter)
    
        
    for i in range(0,len(space_positions)):
        y = int(space_positions[i])
        new_text.insert(y," ")
    
    encoded_word =""
    for i in range(0,len(new_text)):
        
        encoded_word = encoded_word+new_text[i]
        
    print(encoded_word)


def decode_word(text,shift):
    text_list =list()
    blankless_list=[]
    space_positions =list()
    for letter in text:
        text_list.append(letter)
    
    for i in range(0,len(text_list)):
        if text_list[i] == " ":
            space_position = text_list.index(" ")
            space_positions.append(i)

    for blank in text_list:
        if blank.strip():
            blankless_list.append(blank)
    text_list=blankless_list
    ntext=""
    
    for i in range(0,len(text_list)) :
        ntext = ntext + text_list[i]
        
    new_text = list()
    
    for letter in ntext:
        position= alphabet.index(letter)
        position=int(position)
        new_position = position-shift
        if 0<= new_position < len(alphabet):
            new_letter = alphabet[new_position] 
            new_text.append(new_letter)
        else:    
            while new_position<0:

                new_position = new_position + len(alphabet)
                updated_position = new_position

            if updated_position>=0:
                new_letter = alphabet[updated_position] 
                new_text.append(new_letter)
    for i in range(0,len(space_positions)):
        y = int(space_positions[i])
        new_text.insert(y," ")
    dencoded_word =""
    for i in range(0,len(new_text)):
        
        dencoded_word = dencoded_word+new_text[i]
    print(dencoded_word)
 
def main():
    from art import logo
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction =="encode":
        encode_word(text,shift)
        ask= input("Would u like to try again (y/n): ").lower()
        if ask == "y":
            return main()
        else:
            print("Good Bye")
            quit

    elif direction == "decode": 
        decode_word(text,shift)
        ask= input("Would u like to try again(y/n)").lower()
        if ask == "y":
            return main()
        else:
            print("Good Bye")

            quit
    else:
        print("You type wrong command please try again. (encode / decode)")
        return main()
       

main()

