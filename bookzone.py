from app import app,db
from app.models import User,Post

@app.shell_context_processor       #this makes it possile to write flask shell, that opens a python interpretor in context of the flask application (present one)
def make_shell_context():
	return {'db':db,'User':User,'Post':Post}