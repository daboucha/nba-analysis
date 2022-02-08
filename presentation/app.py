from flask import Flask, render_template, request
from prediction import predictScore
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index(score = '', data=[]):
    if request.method == "POST":  
        data = request.form.getlist('players')
        if data:
            y_pred = predictScore(data)
            score=y_pred
    
    return render_template('index.html', score=score, data=data, len=len(data))

if __name__=='__main__':
    app.run()