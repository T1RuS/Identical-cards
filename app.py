from flask import Flask, render_template, flash
from flask import Flask, render_template, request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from game import GameTwo, GameThree, GameFour

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == "POST":
        if request.form['game'] == '2' and len(request.form['login']) > 5:
            print(1)
            return render_template('gameTwo.html', num=GameTwo())
        elif request.form['game'] == '3' and len(request.form['login']) > 5:
            return render_template('gameThree.html', num=GameThree())
        elif request.form['game'] == '4' and len(request.form['login']) > 5:
            return render_template('gameFour.html', num=GameFour())
        else:
            pass
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
