# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import string
import random
from tkinter import messagebox
import pyperclip

def pass_gen():
    pass_entry.delete(0,END)
    letters_lower = list(string.ascii_lowercase)
    letters_upper = list(string.ascii_uppercase)
    numbers = list(string.digits)
    punctuation = list(string.punctuation)

    all_keys = letters_lower+letters_upper+numbers+punctuation

    generated_pass =random.choices(all_keys,k=(random.randint(8,12)))

    final_pass = "".join(generated_pass)

    pass_entry.insert(0,f"{final_pass}")

    pyperclip.copy(final_pass)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_but():
    website =website_entry.get()
    email=email_entry.get()
    password = pass_entry.get()
    

    if website == "" or email=="" or password=="":
        messagebox.showinfo(title="Warning", message="Fill all information Please")
    
    else:    
        save = messagebox.askokcancel(title="Check Point",message=f"You filled your {website},{email} and {password} information would u like to save ? ")
        if save :
            with open("data.txt","a") as file:
                file.write(f"{website} | {email}   | {password}\n")






# ---------------------------- UI SETUP ------------------------------- #

from tkinter import * 
import tkinter as tk
my_screen = Tk()
my_screen.title("Password Generator")
my_screen.config(padx=30,pady=30)
img = PhotoImage(file="logo.png")
canvas = Canvas(width=200,height=200,highlightthickness=0)
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

#Labels
website_label = Label(text="Website: ",highlightthickness=0)
website_label.grid(column=0,row=1,sticky=E)

email_label = Label(text="Email/Username: ",highlightthickness=0)
email_label.grid(column=0,row=2,sticky=E)

pass_label = Label(text="Password: ",highlightthickness=0)
pass_label.grid(column=0,row=3,sticky=E)



#Entry

website_entry = Entry(width=45)

website_entry.grid(column=1,row=1,columnspan=2,sticky=tk.W)
website_entry.focus()
email_entry = Entry(width=45)

email_entry.grid(column=1,row=2,columnspan=2,sticky=tk.W)

pass_entry = Entry(width=32)
pass_entry.grid(column=1,row=3,sticky=tk.W)


#Buttons

generate_button = Button(width=15, text="Generate Password",highlightthickness=0,command=pass_gen)

generate_button.grid(column=2,row=3)


add_button = Button(width=44,text="Add",highlightthickness=0,command=add_but)
add_button.grid(column=1,row=4,columnspan=2,sticky=tk.W)



my_screen.mainloop()