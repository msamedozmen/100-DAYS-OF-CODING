from flask import Flask

from flask_sqlalchemy import SQLAlchemy

#CREATE NEW DATABASE
app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db = SQLAlchemy()
db.init_app(app)

#CREATE NEW TABLE
class Books(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(250), unique = True, nullable=False)
    author = db.Column(db.String(250),nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    
with app.app_context():
    db.create_all()
    
    
#CREATE NEW RECORD

with app.app_context():
    new_book = Books(title="it smasdaasfdssdasdadsase",author ="Samet Ozmen",rating = 9.5)
    db.session.add(new_book)
    db.session.commit()
    
    
#READ ALL RECORDS

with app.app_context():
    result = db.session.execute(db.select(Books).order_by(Books.title))
    all_books = result.scalars()
    
#Read Specific Record by QUERY

with app.app_context():
    book=db.session.execute(db.select(Books).where(Books.title == 'it  me')).scalar()
    
#Update A Particular Record By Query

# with app.app_context():
#     book_to_update=db.session.execute(db.select(Books).where(Books.title =="it  sme")).scalar()
#     book_to_update.title = "Benim"
#     db.session.commit()
    
#Update A Record By PRIMARY KEY
book_id = 1
with app.app_context():
    book = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    book.title ="NEw"
    db.session.delete(book)
    db.session.commit()