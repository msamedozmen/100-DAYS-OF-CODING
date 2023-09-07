from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,InputRequired,ValidationError
from flask_bootstrap import Bootstrap4

def check_email(form,field):
    if "@" not in field.data and "." not in field.data:
        raise ValidationError("You have to use '@' and '.'")
    elif "@" not in field.data:
            raise ValidationError("You have to use '@'")
    elif "." not in field.data:
        raise ValidationError("You have to use '.' ")
    else:
        pass
        
def pass_leng(form,field):
    if len(field.data)<8:
        raise ValidationError("Your psasword should be at least 8 characters")

class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), check_email])
    password = PasswordField("password",validators=[InputRequired(),pass_leng])
    submit = SubmitField(label="Log In")



app = Flask(__name__)
app.secret_key = "its me"
bootstrap = Bootstrap4(app)

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET",'POST'])

def login():
    loginin = LoginForm()
    if loginin.validate_on_submit():
        if loginin.email.data == "admin@email.com" and loginin.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    else:
        return render_template('login.html' ,form = loginin)

if __name__ == '__main__':
    app.run(debug=True)
