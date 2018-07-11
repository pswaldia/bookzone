from app import app,db
from flask import render_template,redirect,flash,url_for
from app.forms import RegistrationForm,LoginForm
from flask_login import current_user,login_user,logout_user
from app.models import User
import pandas as pd
df=pd.read_csv("/Users/pswaldia1/bookzone/app/static/goodread.csv")


@app.route('/login',methods=['GET','POST'])
def login():
	form=LoginForm()
	if current_user.is_authenticated:
		return redirect(url_for('logout'))
	if form.validate_on_submit():
		user=User.query.filter_by(username = form.username.data).first()
		if user is None or not  user.check_password(form.password.data):
			flash('Invalid Username or Password')
			return redirect(url_for('login'))
		login_user(user,remember=form.remember_me.data)
		return render_template('profile.html')
	return render_template('login.html',form=form)	


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('register'))





@app.route('/',methods=['GET','POST'])
@app.route("/register",methods=['GET','POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('logout'))
	registerForm=RegistrationForm()
	loginForm=LoginForm()
	if registerForm.validate_on_submit():
		u=User(username=registerForm.username.data,email=registerForm.email.data)
		u.set_password(registerForm.password.data)
		db.session.add(u)
		db.session.commit()
		flash('congratulations! You are now registered!')
		return redirect(url_for('register'))
	return render_template('forms.html',form1=registerForm,df=df)



        


        
        
        
       

	
		



