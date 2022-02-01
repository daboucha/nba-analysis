from flask import Flask, render_template
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')