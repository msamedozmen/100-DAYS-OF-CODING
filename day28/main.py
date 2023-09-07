
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 0.5
repeat=0
check_mark=""
start_time = None
# ---------------------------- TIMER RESET ------------------------------- #  
def reset():
    my_window.after_cancel(start_time)
    canvas.itemconfig(text_canvas,text="00:00")
    timer_label.config(text="Timer")
    check_label.config(text="")
    global repeat,check_mark
    check_mark=""
    repeat =0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repeat
    global check_mark
    studying = WORK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    long_break = int(LONG_BREAK_MIN*60)
    
    if repeat in range(0,5,2):
        timer_label.config(text="Study Hard")
        count_down(studying)


        repeat+=1
    elif repeat in range(1,4,2):
        timer_label.config(text="Rest Less")
        count_down(short_break)
        check_mark+="✔"
        check_label.config(text=f"{check_mark}")
        repeat+=1
    elif repeat == 5:
        timer_label.config(text="Rest Hard")
        count_down(long_break)
        check_mark+="✔"
        check_label.config(text=f"{check_mark}")
        repeat+=1
    else: 
        canvas.create_text(100,135,fill="white",text="00:00",font=(FONT_NAME,30,"bold"))


        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(sec):
    min = int(sec/60)
    global start_time
    new_sec = sec %60
    if min<10:
        if new_sec<10:
            canvas.itemconfig(text_canvas,text=f"0{min}:0{new_sec}")
        
        else:
            canvas.itemconfig(text_canvas,text=f"0{min}:{new_sec}")
            
    else:
            if new_sec<10:
                canvas.itemconfig(text_canvas,text=f"{min}:0{new_sec}")
        
            else:
                canvas.itemconfig(text_canvas,text=f"{min}:{new_sec}")
    if sec >0:
        start_time =my_window.after(50,count_down,sec-1)
    else:
        start_timer()



   


        
# second =60
# while second>0:
#     count_down(second)
# ---------------------------- UI SETUP ------------------------------- #

from  tkinter import *

my_window = Tk()
my_window.title("BREAK TIMER")
# my_window.minsize(width=400,height=400)
my_window.configure(padx=100,pady=100,bg=PINK)

    
img = PhotoImage(file="tomato.png")
# photo = Label(my_window, bg =PINK, image = img)
# photo.pack()
# time = Label(text="00:00", font=(FONT_NAME,30,"bold"),bg=RED,highlightcolor="red")
# time.place(x=100,y=120)
canvas = Canvas(width=200,height=224,bg=PINK,highlightthickness=0)
canvas.create_image(100,112,image=img)
text_canvas=canvas.create_text(100,135,fill="white",text="00:00",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)
# count_down(second)
#Timer Label
timer_label =Label(text="Timer", font=(FONT_NAME,30,"bold"),bg=PINK,fg=GREEN,highlightthickness=0)

timer_label.grid(column=1,row=0)
timer_label.grid
#Start Button
start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)
#Reset Button
reset_button = Button(text="Reset",highlightthickness=0,command=reset)
reset_button.grid(column=2,row=2)

#Check label
check_label = Label(text="", font=(FONT_NAME,15,"bold"),bg=PINK,fg=GREEN,highlightthickness=0)
check_label.grid(column=1,row=4)


    
my_window.mainloop()

