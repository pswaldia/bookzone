from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,EqualTo,ValidationError

class RegistrationForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired()])
	email=StringField('Email',validators=[DataRequired()])
	password=PasswordField('Password',validators=[DataRequired()])
	password2=PasswordField('Repeat Password',validators=[DataRequired(),EqualTo('password')])
	submit=SubmitField('Register')

	def validate_username(self,username):
		user=User.query.filter_by(username=username.data).first()   #this will query the user
		if user is not None:
			raise ValidationError('username not available')

	def validate_email(self,email):
		email=User.query.filter_by(email=email.data).first()
		if email is not None:
			raise ValidationError('email is already registered')

class LoginForm(FlaskForm):
	username=StringField('username',validators=[DataRequired()])
	password=StringField('Password',validators=[DataRequired()])
	remember_me=BooleanField('Remember me')
	submit=SubmitField('Login')







