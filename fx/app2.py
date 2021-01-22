from flask import Flask, render_template, request, flash
from wtforms import Form, FloatField, SubmitField, validators, ValidationError, StringField, IntegerField
import numpy as np
import math
import joblib

def predict(parameters):
    model = joblib.load('./model.pkl')
    pred = model.predict(parameters)

    return pred


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'zJe09C5c3tMf5FnNL09C5d6SAzZoY'



@app.route('/', methods = ['GET', 'POST'])
def predicts():

    if request.method == 'POST':

        money = request.form["money"]
        money = np.array(money.split(','))
        input_test = np.reshape(money, (1, 10, 1))
        print(money)
        print(input_test.shape)

        pred = predict(input_test)

        return render_template('result.html', pred = pred)
    elif request.method == 'GET':
        return render_template('index2.html')

if __name__ == "__main__":
    app.run()
