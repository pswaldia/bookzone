from app import app
from flask import render_template
from app.forms import RegistrationForm,LoginForm

@app.route("/")
def index():
	registerForm=RegistrationForm()
	loginForm=LoginForm()
	return render_template("forms.html",form1=registerForm,form2=loginForm)


