from tkinter import *
 
import requests

kanye_url ="https://api.kanye.rest"


def quote_button():
    response = requests.get(url=kanye_url)
    quotes = response.json()["quote"]

    canva.itemconfig(canva_text,text=f"{quotes}")

    

#SET UP WINDOW
my_screen = Tk()
my_screen.title("Kanye's quote")
my_screen.configure(padx=50,pady=50)
canva = Canvas(width=300,height=414,highlightthickness=0)
bg_img = PhotoImage(file="background.png")
my_bg = canva.create_image(150,207,image=bg_img)
canva.grid(column=0,row=0)

# TEXT
canva_text = canva.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="white")

#Create Button

button_img = PhotoImage(file="kanye.png")
button = Button(image=button_img,command=quote_button)
button.grid(column=0,row=1)
my_screen.mainloop()

