from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///new-books-collection.db"
db = SQLAlchemy()
db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String, unique = True, nullable = False)
    author = db.Column(db.String,nullable=False)
    rating = db.Column(db.Float,nullable=False)

with app.app_context():
    db.create_all()
    
    
@app.route('/')
def home():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()
    return render_template("index.html",books=all_books)


@app.route("/add",methods = ["GET","POST"])
def add():
    if request.method == "POST":
        with app.app_context():
            new_book = Books(title=f"{request.form['title']}",author =f"{request.form['author']}",rating = f"{request.form['rating']}")
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        #UPDATE RECORD
        
        book_id = request.form["id"]
        with app.app_context():
            book_to_update = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
            book_to_update.rating = request.form["rating"]
            db.session.commit()
            return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected =  db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    return render_template("edit.html", book=book_selected)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')

    with app.app_context():
        book_to_delete =  db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()
        return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)

