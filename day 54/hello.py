
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1>' \
            "<p> Banageeee </p>" \
            '<img src= "https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif" widht=400 >'
@app.route("/ye")
def bye():
    return "Byeeeeeee"
print(__name__)

@app.route("/username/<name>")
def great(name):
    return f"Hello {name}"

if __name__ =="__main__":
    app.run(debug=True)