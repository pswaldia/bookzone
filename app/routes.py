from app import app
from flask import render_template,redirect,flash
from app.forms import RegistrationForm,LoginForm
from flask_login import current_user,login_user,logout_user
from app.models import User
@app.route("/",methods=['GET','POST'])
def index():
	registerForm=RegistrationForm()
	
	if current_user.is_authenticated:
		return render_template('profile.html')
	loginForm=LoginForm()
	if loginForm.validate_on_submit():
		user=User.query.filter_by(username=loginForm.username.data).first()
		if user is None or not user.check_password(loginForm.password.data):
			flash('Invalid username or password')
			return redirect('/')
		login_user(user,remember=loginForm.remember_me.data)  #this handles the login of the user 
		return redirect('/')
	return render_template('forms.html',form2=loginForm,form1=registerForm)		
@app.route('/profile')
def logout():
    logout_user()
    return redirect('/')




