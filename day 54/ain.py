from flask import Flask

app = Flask(__name__)
import random
random_number = random.randint(0, 9)

print(random_number)
@app.route("/")
def open_page():
    return '<h1 style="color:blue"> Welcome to Higher-Lower Game</h1>' \
            '<h2 style="text-align:center"> Please Guess a number between 0-9 </h2>' \
            '<img  style="text-align:center" src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=50%>'
def guess_number_page(funtion):
    def wrapper(guess_number):
        if guess_number > random_number:
            return "<h1 style='color: purple'>Too high, try again!</h1>" \
                "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"

        elif guess_number < random_number:
            return "<h1 style='color: red'>Too low, try again!</h1>"\
                "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
        else:
            return funtion(guess_number)               
    return wrapper
@app.route("/<int:guess_number>")
@guess_number_page

def final(guess_number):
    return "<h1 style='color: green'>You found me!</h1>" \
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"     

                



if __name__ =="__main__":
    app.run(debug=True)