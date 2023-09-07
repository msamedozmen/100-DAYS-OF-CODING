from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random as rd
import json
from sqlalchemy import select

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''



app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:

            dictionary[column.name] = getattr(self, column.name)
        return dictionary    

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")
    


@app.route("/random", methods = ["GET"])
def random_cafe():
    cafes = db.session.execute(db.select(Cafe)) 
    cafes = cafes.scalars().all()
    random_cafe = rd.choice(cafes)
    print(type(random_cafe))
    # return jsonify(cafe={
    #     "id": random_cafe.id,
    #     "name": random_cafe.name,
    #     "map_url": random_cafe.map_url,
    #     "img_url": random_cafe.img_url,
    #     "location": random_cafe.location,
    #     "seats": random_cafe.seats,
    #     "has_toilet": random_cafe.has_toilet,
    #     "has_wifi": random_cafe.has_wifi,
    #     "has_sockets": random_cafe.has_sockets,
    #     "can_take_calls": random_cafe.can_take_calls,
    #     "coffee_price": random_cafe.coffee_price,
    # })
    
    # #or 
    return jsonify(cafe=random_cafe.to_dict())


@app.route("/all",methods = ["GET"])

def all_cafes():
    all_cafes = db.session.execute(db.select(Cafe).order_by(Cafe.id)).scalars().all()
    
    return jsonify(cafes = [cafe.to_dict() for cafe in all_cafes])
## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record

@app.route("/search", methods = ["GET"])
def search_cafe():
    location = request.args.get("location")
    cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()
    
    if cafes:
        return jsonify(cafes = [cafe.to_dict() for cafe in cafes])
    else:
        return jsonify(error = {"Not Found":"There is no cafe in that location"})
    
@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        has_sockets=bool(request.form.get("has_sockets")),
        has_toilet=bool(request.form.get("has_toilet")),
        has_wifi=bool(request.form.get("has_wifi")),
        can_take_calls=bool(request.form.get("can_take_calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

@app.route("/update-price/<int:cafe_id>",methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe= db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id))
    if cafe:
        cafe.coffe_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the new coffee price."})
    else:
        return jsonify(error = {"Not Found":"There is no cafe in that id"}),404
    
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id):
    api_key =request.args.get("api-key")
    if api_key=="TopSecretAPIKey":
        cafe =db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
if __name__ == '__main__':
    app.run(debug=True)
