from flask import Flask, render_template,request
from datetime import date
import smtplib
import requests

response = requests.get(url="https://api.npoint.io/4ac9c32a945d3983ac66")
blog_data = response.json()

def sent_message(name,email,phone,message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    my_email = "sametto0603@gmail.com"
    my_pass ="ulkbhcbvfrnbqjtf"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email,password=my_pass)
    connection.sendmail(from_addr=my_email,to_addrs="sametozo@yahoo.com",msg=email_message)
    
    
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html" ,posts = blog_data)

@app.route('/about/')
def get_about():
    return render_template('about.html')

@app.route("/mypost/<int:id>")
def get_content(id):
    my_website = blog_data[id-1]
    return render_template('post.html', post = my_website)
    

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        sent_message(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

if __name__ =="__main__":
    app.run(debug=True)
    
    

