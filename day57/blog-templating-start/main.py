from flask import Flask, render_template
import requests
from post import Post

blogs_list=[]
response=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blogs = response.json()
for blog in blogs:
    blog_obj = Post(blog["id"], blog["title"], blog["subtitle"], blog["body"])
    blogs_list.append(blog_obj)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",blogs=blogs_list)

@app.route("/post/<int:index>")
def blog_post(index):
    for post in blogs_list:
        if post.id == index:
            my_post = post
            
    return render_template("post.html",post = my_post)
if __name__ == "__main__":
    app.run(debug=True)
    
