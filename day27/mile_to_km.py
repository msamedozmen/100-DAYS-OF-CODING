from tkinter import*

# my_window = Tk()

# my_window.title("Mile to Km")

# # my_window.minsize(width=200,height=200)
# my_window.config(padx=20,pady=20)

# def button_clicked():
#     mil =entry.get()
#     km = round(int(mil)*1.609,1)
#     calculated_label.config(text=f"{km}")
# #Entry

# entry = Entry(width=10,)
# entry.insert(END,string="0")

# entry.grid(column=1,row=0)

# #Labels

# miles_label = Label(text="Miles")
# miles_label.grid(column=2,row=0)

# is_equal_to_label = Label(text="is equal to")
# is_equal_to_label.grid(column=0,row=1)

# calculated_label = Label(text="0")
# calculated_label.grid(column=1,row=1)

# km_label = Label(text="Km")
# km_label.grid(column=2,row=1)

# #Button
# button = Button(text="Calculate",command=button_clicked)
# button.grid(column=1,row=2)


# my_window.mainloop()

my_window = Tk()
my_window.minsize(width=200,height=200)
my_window.title("Mile To Km")

#Entry
entry = Entry(width=5)
entry.insert(END,string="0")
entry.grid(column=1,row=0)

#Labels
label1 = Label(text="Miles")
label1.grid(column=2,row=0)

label2 = Label(text="is equal to")
label2.grid(column=0,row=1)

label4 = Label(text=f"{entry.get()}")
label4.grid(column=1,row=1)

label5 = Label(text="Km")
label5.grid(column=2,row=1)


#Button
def but():
    
    mil =entry.get()
    km = round(int(mil)*1.609,2)
    label4.config(text=f"{km}")
    
button = Button(text="Calculate",command=but)
button.grid(column=1,row=2)
my_window.mainloop()