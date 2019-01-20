from flask import Flask
from flask import request
from flask_login import LoginManager
from os import getenv
import json
import pypyodbc

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

connection = pypyodbc.connect('Driver={SQL Server};Server=bdallovelo.c4hn4wmypuno.us-east-2.rds.amazonaws.com;Database=DBO;uid=PolyHxAlloVelo;pwd=2chocolats')

@app.route("/")
def hello():
    return "Hello World!"

#signup
@app.route("/api/signup", methods=['POST'])
def signup():
    content = request.json
    
    email = content['email']
    firstname = content['name']
    password = content['password']

    cursor = connection.cursor() 
    SQLCommand = "INSERT INTO [user] (email, firstname, password) VALUES (?,?,?)" 
    Values = [email,firstname,password] 
    cursor.execute(SQLCommand,Values) 
    connection.commit()
    
    return 'signup'

#login
@app.route('/api/login', methods=['GET', 'POST'])
def login():
    content = request.json   
    email = content['email']
    password = content['password']

    
    return "login"

#logout
@app.route("/api/logout")
def logout():
    logout_user()
    return redirect(somewhere)

@app.route("/api/google", methods=['get'])
def google():
    return 'google'

if __name__ == '__main__':
  app.run(host='0.0.0.0')

  