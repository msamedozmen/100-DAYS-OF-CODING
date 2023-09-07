from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

# app = Flask(__name__)
# app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Bootstrap5(app)

# app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///posts.db"

# db = SQLAlchemy()
# db.init_app(app)

class PostForm(FlaskForm):
    title = StringField("Blog Post Title",validators=[DataRequired()])
    subtitle=StringField("Subtitle",validators=[DataRequired()])
    name = StringField("Your Name",validators=[DataRequired()])
    img_url = StringField("Blog Image URL",validators=[DataRequired(),URL()])
    body = CKEditorField("Blog Content",validators=[DataRequired()])
    submit = SubmitField("Publish Your Post")
    
    
# class BlogPost():
#     id = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.String,unique = True,nullable=False)
#     subtitle = db.Column(db.String,nullable=False)
#     body = db.Column(db.Text,nullable = False)
#     img_url = db.Column(db.String,nullable=False)
#     date = db.Column(db.String,nullable =False)
#     author = db.Column(db.String,nullable=False)
    
    
    
# with app.app_context():
#     db.create_all()
    
    
# @app.route("/")
# def gel_all_posts():
#     posts = db.session.execute(db.select(BlogPost)).scalars().all()
#     return render_template("index.html",all_posts = posts)



app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy()
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


with app.app_context():
    db.create_all()


@app.route('/')
def get_all_posts():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/post/<int:post_id>')
def show_post(post_id):

    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    return render_template("post.html", post=requested_post)

@app.route("/add-post", methods = ["GET","POST"])
def add_new_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            title=form.title.data,
            subtitle = form.subtitle.data,
            img_url = form.img_url.data,
            author=form.name.data,
            body = form.body.data,
            date=date.today().strftime("%B, %d, %Y")
        )
        
        
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)

@app.route("/edit-post/<post_id>",methods = ["GET","POST"])
def edit_post(post_id):
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    edite_form = PostForm(
        title=requested_post.title,
        subtitle=requested_post.subtitle,
        img_url=requested_post.img_url,
        name=requested_post.author,
        body=requested_post.body
                )
    if edite_form.validate_on_submit():

        requested_post.title = edite_form.title.data
        requested_post.subtitle = edite_form.subtitle.data
        requested_post.img_url = edite_form.img_url.data
        requested_post.author = edite_form.name.data
        requested_post.body = edite_form.body.data    
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))

        
    
    return render_template("make-post.html",form = edite_form, is_edit = True)

@app.route('/delete/<int:post_id>')
def delete(post_id):
    requested_post = db.session.execute(db.select(BlogPost).where(BlogPost.id == post_id)).scalar()
    db.session.delete(requested_post)
    db.session.commit()

    return redirect(url_for('get_all_posts'))

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
