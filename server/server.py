from flask import request
from flask import Flask, render_template
from os import getenv
import json
import googleApi

app = Flask(__name__, static_folder = "./dist", template_folder = ".")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

#signup
@app.route("/api/signup", methods=['POST'])
def signup():
    content = request.json
    
    with open('./database/users.json', 'r+') as file:
        data = json.load(file)
        for item in data :
            if item['email'] == content['email']:
                return 'error 403'
        data.append(content)
        file.seek(0)
        json.dump(data, file)
        file.truncate()
            
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
  print ('a')

@app.route("/api/google/<string:lat>/<string:lon>", methods=['GET'])
def google(lat, lon):
    return googleApi.googleApi(lat, lon).getData()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

  