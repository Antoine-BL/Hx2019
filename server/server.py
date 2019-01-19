from flask import Flask
from os import getenv
import json
import pypyodbc

app = Flask(__name__)


connection = pypyodbc.connect('Driver={SQL Server};Server=bdallovelo.c4hn4wmypuno.us-east-2.rds.amazonaws.com;Database=DBO;uid=PolyHxAlloVelo;pwd=2chocolats')

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/signup", methods=['PUT'])
def signup():
    return 'signup'

@app.route("/api/google", methods=['get'])
def google():
    return 'google'

if __name__ == '__main__':
  app.run(host='0.0.0.0')