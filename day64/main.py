from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

my_api = "0e90f54358c029c572d47a24ea8d2c9a"
url= "https://api.themoviedb.org/3/search/movie"
search_url ="https://api.themoviedb.org/3/movie"
image_url_api = "https://image.tmdb.org/t/p/w500"
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies-collections.db'

Bootstrap5(app)

db = SQLAlchemy()
db.init_app(app)

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)
    
with app.app_context():
    db.create_all()

class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")
    
class AddMovie(FlaskForm):
    title = StringField("Please insert Movie Title")
    add = SubmitField("Add Movie")
# new_movie = Movies(
#     title="Phone",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()
# second_movie = Movies(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(second_movie)
#     db.session.commit()

@app.route("/")
def home():
    result = db.session.execute(db.select(Movies).order_by(Movies.rating))
    all_movies = result.scalars().all()[::-1]
    for i in range(len(all_movies)):
        all_movies[i].ranking = i+1
    db.session.commit()
    return render_template("index.html", movies = all_movies)


@app.route('/edit', methods = ["GET","POST"])
def edit():
    form = RateMovieForm()
    movie_id =request.args.get("id")
    movie = db.session.execute(db.select(Movies).where(Movies.id ==movie_id)).scalar()
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html', movie=movie,form=form)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    with app.app_context():
        movie = db.session.execute(db.select(Movies).where(Movies.id == movie_id)).scalar() 
        db.session.delete(movie)
        db.session.commit()
    return redirect(url_for("home"))
    
@app.route('/add',methods=["GET","POST"])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        new_movie_title = form.title.data
        response = requests.get(url=url, params={"api_key": my_api, "query": new_movie_title})
        datas = response.json()["results"]
        return render_template("select.html", datas=datas)
    return render_template("add.html",form=form)   


@app.route('/selected')
def selected():
    movie_id_api = request.args.get("id")
    if movie_id_api:
        response = requests.get(url=f"{search_url}/{movie_id_api}",params={"api_key": my_api,"language": "en-US"})
        data =response.json()
        new_movie = Movies(
            title=data["title"],
            year = data["release_date"].split("-")[0],
            description = data["overview"],
            img_url=f"{image_url_api}{data['poster_path']}"
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))

if __name__ == '__main__':  
    app.run(debug=True)

