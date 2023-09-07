from tkinter import *


new_window = Tk()
new_window.title("Test")
new_window.minsize(600,400)


# Create Label

my_label = Label(text="I am a label", font=("Arial",24,"bold"))
my_label.pack()

#Change label 
my_label["text"] = "Samet"
my_label.config(text="rem")


#button
def button_clicked():
    # print("I clicked")
        new_text = input.get()

    my_label["text"] = "Samet"


button = Button(text="Click me",command=button_clicked)
button.pack()


#Entry component

def input_str():
    new_text = input.get()
    my_label["text"] =  new_text
    
input = Entry(width=10,bg="red")

input.pack()
print(input.get())

new_window.mainloop()

# *args

# def add(*args):
#     score =0
#     for number in args:
#         score +=number
#     print(score)
        
# add(1,2,3,4,5,6,7)


# def calculator(n,**kwargs):
#     n+=kwargs["add"]
#     n*=kwargs["multiple"]
#     return n
    
    
# calculator(10,add=11,multiple=12)
# print(calculator(10,add=11,multiple=12))


# class Car:  
#     def __init__(self,**kwargs):
        
#         # self.model = kwargs["model"]
#         # self.price = kwargs["Price"]
        
#         self.model=kwargs.get("model")
#         self.price = kwargs.get("Price")
# car = Car(model=" BMW ", Price = 189)

# print(car.price)
