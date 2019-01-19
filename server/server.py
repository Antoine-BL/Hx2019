from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/signup", methods=['get'])
def signup():
    return 'signup'

@app.route("/api/google", methods=['get'])
def google():
    return 'google'

if __name__ == '__main__':
  app.run(host='0.0.0.0')