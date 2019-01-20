from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import Flask, render_template, request
from os import getenv
import json
import googleApi

app = Flask(__name__, static_folder = "./dist", template_folder = ".")
app.secret_key = 'super secret string'

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(email):
    with open('./database/users.json', 'r+') as file:
        isGood = False
        data = json.load(file)
        for item in data :
            if item['email'] == email:
                isGood = True
        if not isGood:
            return

    user = User()
    user.id = email
    return user

# @login_manager.request_loader
# def request_loader(request):
#     email = request.json['email']
#     with open('./database/users.json', 'r+') as file:
#         isGood = False
#         data = json.load(file)
#         for item in data :
#             if item['email'] == request.json['email'] and item['password'] == request.json['password']:
#                 isGood = True
#         if not isGood:
#             return

#     user = User()
#     user.id = email
#     user.is_authenticated = True

#     return user

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

    with open('./database/users.json', 'r') as file:
        data = json.load(file)
        for user in data:
            if user['email'] == email and user['password'] == password :
                user = User()
                user.id = email
                login_user(user)
                return 'yup'#redirect(url_for('protected'))
    
    return "invalid"


@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + current_user.id

#logout
@app.route("/api/logout", methods=['POST'])
def logout():
    logout_user()
    return 'Logged out'

@app.route('/api/joingroup', methods=['POST'])
@login_required
def joinGroup():
    content = request.json   
    id = content['id']

    with open('./database/groups.json', 'r+') as file:
        data = json.load(file)
        for group in data:
            if group['id'] == id:
                group['members'].append(current_user.id)
                file.seek(0)
                json.dump(data, file)
                file.truncate()
                return 'group joined'

    return 'error'

@app.route("/api/creategroup", methods=['POST'])
@login_required
def createGroup():
    content = request.json
    
    with open('./database/groups.json', 'r+') as file:
        data = json.load(file)
        data.append({
            "id": 2,
            "creator": current_user.id,
            "members": [],
            "date": content['date']
        })
        file.seek(0)
        json.dump(data, file)
        file.truncate()
            
    return 'group created'


@app.route("/api/google/<string:lat>/<string:lon>", methods=['GET'])
def google(lat, lon):
    return googleApi.googleApi(lat, lon).getData()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

  