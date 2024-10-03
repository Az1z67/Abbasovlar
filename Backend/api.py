import sqlite3 
import json
from flask import Flask, request, jsonify, render_template #type: ignore


app  = Flask(__name__)

@app.get("/")
def index():
  return render_template('templates/index.html')

app.run(host='0.0.0.0', port=5040)