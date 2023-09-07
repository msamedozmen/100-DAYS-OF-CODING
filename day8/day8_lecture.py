def great():
    
    print("hello")
    
great()

#Function with one inouts
def great_with_name(name):
    print(f"Hello {name}")

great_with_name("Samet")

#function with more than one inputs

def great_with(name,location):
    print(f"Hello {name}")
    print(f" is your location {location}?")
    
great_with("Samet","Ankara")


#function with keyword argument


def keyword(a = 2 ,b=3 ,c=4):
    print(a+b+c)