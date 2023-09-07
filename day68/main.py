from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
# CREATE TABLE IN DB



class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
@login_manager.user_loader
def load_user(user_id):
        return db.get_or_404(User,user_id)

 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html",logged_in=current_user.is_authenticated)


@app.route('/register',methods = ["GET","POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = db.session.execute(db.select(User).where(User.email ==email)).scalar()
        
        if user:
            flash("You already enrolled")
            return redirect(url_for("login"))
        else:
            
            hash_and_salted_password = generate_password_hash(
                request.form.get('password'),
                method='pbkdf2:sha256',
                salt_length=8
            )
            
                
            new_user = User(
                email=request.form.get('email'),
                name=request.form.get('name'),
                password=hash_and_salted_password
            )
            db.session.add(new_user)
            db.session.commit()
            
            login_user(new_user)

            return render_template("secrets.html",user= new_user)
    return render_template("register.html")


@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = db.session.execute(db.select(User).where(User.email ==email)).scalar()
        if  not user:
            flash("This mail not exist please register or check spells")
            return redirect(url_for('login'))

        elif not check_password_hash(user.password,password):
            flash('Password incorrect, please try again.')
            return redirect(url_for("login"))
        else:
            login_user(user)
            return redirect(url_for("secrets"))

    return render_template("login.html")


@app.route('/secrets')
@login_required

def secrets():
    
    return render_template("secrets.html",name = current_user.name)


@app.route('/logout')
@login_required

def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download_file():
    return send_from_directory('static', path="files/cheat_sheet.pdf")
    

if __name__ == "__main__":
    app.run(debug=True)
