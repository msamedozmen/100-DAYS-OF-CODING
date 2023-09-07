#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
        

with open("Users\MONSTER\Desktop\Udemy\day24\ene\MailMergeProjectStart\Input\jamesinvited_names.txt") as file:
    lines =file.readlines()

with open("MailMergeProjectStart\Input\Letters\starting_letters.txt") as f:
    letters= f.read()
    letters.strip()
    for line in lines:
        line=line.strip()
        letters.replace("[name]",line)
        # with open(f"day24\Mail+Merge+Project+Start\Mail Merge Project Start\Input\Letters\somebody_{line}.txt") as f:
        #     f.write()
    print(letters)    

