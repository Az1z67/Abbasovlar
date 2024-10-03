import sqlite3 
import json
from flask import Flask, request, jsonify #type: ignore


app  = Flask(__name__)

@app.get("/hello")
def hello_world():
  return 'Hello World!'

app.run(host='localhost', port=5040)