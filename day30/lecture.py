try :
    file = open("text.txt")
    a_dict ={"key":"value"}
    print(a_dict["key"])
except FileNotFoundError:
    file = open("text.txt","w")
    file.write("ben")
except KeyError as error_message:
    print(f"{error_message} is not exist")
    
else:
    cont = file.read()
    print(cont)