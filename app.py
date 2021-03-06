from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
print "ENVIRNOMENT IS %s" %(os.environ['APP_SETTINGS'])

from models import Result

@app.route('/')
def hello():
	return "Hello world"

@app.route('/<name>')
def hello_name(name):
	return "Hello %s" %(name)

if __name__ == '__main__':
	app.run()