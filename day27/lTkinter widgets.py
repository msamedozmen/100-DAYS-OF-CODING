from tkinter import *


#Create Window
my_window = Tk()
my_window.title("TEST")
my_window.minsize(width=300,height=300)
my_window.config(padx=20,pady=20)
#Create Label


my_label = Label(text="Test Text")
my_label.config(text="Changed text")#new text
my_label.pack()
# my_label.place(x=0,y=0)
# my_label.grid(column=0,row=0)
#Buttons

def button_action():
    new_text = entry.get()
    # new_text2 = text.get("1.0",END) #(1.0) mean is line 1 and first letter
    # spin = spinbox.get()
    # my_label.config(text=f"{spin} \n{new_text} {new_text2}")
    my_label.config(text=f"{new_text}")

button = Button(text="Hit Here", command=button_action)
button.pack()
# button.grid(column=1,row=1)

button2 = Button(text="Hit Here", command=button_action)
button.pack()
# button2.grid(column=2,row=0)

#Entries
    
entry = Entry(width=30,bg="pink",)
entry.insert(END,string="Put your name")
entry.pack()
# entry.grid(column=3,row=2)

#Text

text = Text(width=10,height=10)
text.insert(END,"Fill your surname")
text.pack()


#spinbox
def spin_used():
    spins = spinbox.get()
    print(spins)
spinbox = Spinbox(width=1,from_= 0, to= 10,bg="red",command=spin_used)
spinbox.pack()

#Scale
def scale_used(value):
    print(value)
    
scale = Scale(bg="blue",from_=0,to=100,command=scale_used)
scale.pack()

#Check Button
def check_button_used():
    print(check_state.get())
check_state = IntVar()
check_button = Checkbutton(text="Is On? ",variable=check_state,command=check_button_used)
check_state.get()
check_button.pack()

#Radio Buttom

def radio_used():
    print(radio_button_state.get())
radio_button_state = IntVar()

radio_button1 = Radiobutton(text="Option 1",variable=radio_button_state,command=radio_used,value=1)
radio_button2 = Radiobutton(text="Option 2",variable=radio_button_state,command=radio_used,value=2)
radio_button1.pack()
radio_button2.pack()


#List Box

list_box = Listbox(width=5)
names = ["Ahmet","Emre","Samed","Murat","Aysel"]
def listbox_used(event):
    print(list_box.get(list_box.curselection()))
    
for name in names:
    list_box.insert(names.index(name),name)
    
list_box.bind("<<ListboxSelect>>",func= listbox_used)
    
list_box.pack()




my_window.mainloop()