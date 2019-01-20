from flask import request
from flask_login import LoginManager
from flask import Flask, render_template
from os import getenv
import json
import pypyodbc
import googleApi

app = Flask(__name__, static_folder = "./dist", template_folder = ".")

login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

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

@app.route("/api/google/<string:lat>/<string:lon>", methods=['GET'])
def google(lat, lon):
    return googleApi.googleApi(lat, lon).getData()

if __name__ == '__main__':
  app.run(host='0.0.0.0')

  