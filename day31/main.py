BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random

#-------------------------------------------READ DATA------------------------------------------------------------
data = pd.read_csv("zfrench_words.csv")
data_dict ={row.French: row.English for (index,row) in data.iterrows()}

English_list = list(data_dict.values())
French_list = list(data_dict.keys())

# print(English_list)
# print(French_list)
Learned_English =[]
learned_French = []
random_word = random.randint(0,len(English_list)-1)
#--------------------------------------------- SWITCH WORDS -------------------------   -----------------------------
def unknown_word():
    global random_word

    is_new = True
    while is_new:
        random_word = random.randint(0,len(English_list)-1)
        if English_list[random_word] not in Learned_English:
            canvas.delete(0,END)
            canvas.itemconfig(title,text="French",fill="black")
            # a=canvas.create_text(400,263,text=f"{French_list[random_word]}",font=("Ariel",60,"bold"))
            canvas.itemconfig(word,text =f"{French_list[random_word]}",font=("Ariel",60,"bold"),fill="black")
            canvas.itemconfig(front,image=front_img)

            my_screen.after(3000,func=flip_card)
            is_new=False
def known_word():
    global random_word
    learned_French.append(French_list[random_word])
    Learned_English.append(English_list[random_word])
    French_list.remove(French_list[random_word])
    English_list.remove(English_list[random_word])

    is_new = True
    while is_new:
        random_word = random.randint(0,len(English_list)-1)
        if English_list[random_word] not in Learned_English:
            canvas.delete(0,END)
            canvas.itemconfig(front,image=front_img)
            canvas.itemconfig(title,text="French",fill = "white")
            # a=canvas.create_text(400,263,text=f"{French_list[random_word]}",font=("Ariel",60,"bold"))
            canvas.itemconfig(word,text =f"{French_list[random_word]}",font=("Ariel",60,"bold"),fill="white")    
            my_screen.after(3000,func=flip_card)
            is_new = False

def flip_card():

        canvas.itemconfig(title,text="English",fill="white")
        canvas.itemconfig(word,text =f"{English_list[random_word]}",font=("Ariel",60,"bold"),fill="white")    
        canvas.itemconfig(back,image=back_img)


#---------------------------------------------UI SETUP------------------------------------------------------------
#Screen 
my_screen = Tk()

my_screen.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
my_screen.title("Flash Card")
#Canvas
front_img = PhotoImage(file="images\card_front.png")
canvas=Canvas(width=800,height=526)
front =canvas.create_image(400,263,image=front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)

back_img = PhotoImage(file="images\card_back.png")
back = canvas.create_image(400,263,image=back_img)

title =canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"))
word =canvas.create_text(400,263,text=f"{French_list[random_word]}",font=("Ariel",60,"bold"),fill="black")
canvas.grid(column=0,row=0,columnspan=2)
my_screen.after(3000,func=flip_card)
#Button
my_image = PhotoImage(file="images\zright.png")
green_button = Button(image=my_image, highlightthickness=0,command=known_word)
my_image2 = PhotoImage(file="images\wrong.png")
red_button = Button(image=my_image2, highlightthickness=0,command=unknown_word)
green_button.grid(column=1,row=1)
red_button.grid(column=0,row=1)


my_screen.mainloop()
    
learned_dict = {learned_French[x]:Learned_English[x] for x in range(len(learned_French))}
print(learned_French)
print(Learned_English)
print(len(English_list))
print(len(French_list))
words_to_learn = {French_list[x]:English_list[x] for x in range(len(English_list))}

print(words_to_learn)
df = pd.DataFrame(words_to_learn.items(),columns=['French','English'])
a=df.to_csv("words_to_learn.csv",index=4)


