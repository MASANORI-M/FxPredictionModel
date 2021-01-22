from flask import Flask, render_template, request, flash
from wtforms import Form, FloatField, SubmitField, validators, ValidationError, StringField, IntegerField
import numpy as np
import math
import joblib

def predict(parameters):
    model = joblib.load('./model.pkl')
    params = parameters.reshape(1, -1)
    pred = model.predict(params)


app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'zJe09C5c3tMf5FnNL09C5d6SAzZoY'

class DateForm(Form):
    date = StringField("今日の日付(入力例：2020-12-16)",
                            [validators.InputRequired("この項目は入力必須です"),
                            validators.NumberRange(min = 1, max = 20)])

    money = IntegerField("今日の終値",
                            [validators.InputRequired("この項目は入力必須です"),
                            validators.NumberRange(min = 1, max = 20)])

    submit = SubmitField("予測")

@app.route('/', methods = ['GET', 'POST'])
def predicts():
    form = DateForm(request.form)

    if request.method == 'POST':
        if form.validate() == False:
            flash("入力してください")
            return render_template('index.html', form = form)
        else:
            date = request.form["date"]
            print(date)
            print(type(date))

            money = int(request.form["money"])
            print(money)
            print(type(money))

            x = np.array([date, money])
            print(x)
            pred = predict(x)

            return render_template('result.html', datepred = pred)
    elif request.method == 'GET':
        return render_template('index.html', form = form)

if __name__ == "__main__":
    app.run()
