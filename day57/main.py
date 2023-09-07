from flask import Flask, render_template
import random
import datetime as dt
import requests


app = Flask(__name__)




@app.route('/')
def home():
    random_number = random.randint(0,100)
    
    return render_template("home.html",random_number=random_number)


@app.route('/guess/<name>')
def guess(name):

    response1= requests.get(f"https://api.genderize.io?name={name}")
    gender = response1.json()["gender"]
    response2= requests.get(f"https://api.agify.io?name={name}")
    age = response2.json()["age"]
    return render_template("index.html",name=name,gender=gender,age=age)

@app.route('/blog/<num>')
def get_blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    
    app.run(debug=True)
