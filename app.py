from flask import Flask, flash, jsonify
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from game import GameTwo, GameThree, GameFour


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(300), nullable=False)
    game = db.Column(db.String(300), nullable=False)
    status = db.Column(db.String(300), nullable=True)



@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == "POST":
        if request.form['game'] == '2' and len(request.form['login']) > 5:
            login = request.form['login']
            game_num = GameTwo()
            new_game = Register(login=login, game=game_num, status=0)
            try:
                db.session.add(new_game)
                db.session.commit()
                game_id = db.session.query(Register).order_by(Register.id)[-1]
            except:
                return "Ошибка сохранения"
            return render_template('gameTwo.html', game_id=game_id)  # добавить айди нового пользователя
        elif request.form['game'] == '3' and len(request.form['login']) > 5:
            login = request.form['login']
            game_num = GameThree()
            new_game = Register(login=login, game=game_num, status=0)
            try:
                db.session.add(new_game)
                db.session.commit()
                game_id = db.session.query(Register).order_by(Register.id)[-1]
            except:
                return "Ошибка сохранения"
            return render_template('gameThree.html', game_id=game_id)
        elif request.form['game'] == '4' and len(request.form['login']) > 5:
            login = request.form['login']
            game_num = GameFour()
            new_game = Register(login=login, game=game_num, status=0)
            try:
                db.session.add(new_game)
                db.session.commit()
                game_id = db.session.query(Register).order_by(Register.id)[-1]
            except:
                return "Ошибка сохранения"
            return render_template('gameFour.html', game_id=game_id)
        else:
            pass
    return render_template('index.html')


@app.route('/lose', methods=['GET'])
def lose():
     return render_template('Lose.html', game_id=1)


status_num = 0


@app.route('/update', methods=['POST', 'GET'])
def updateNum():
    global status_num
    print(request.form['game_id'])  # принять значения данных ajax
    session_game = Register.query.get(request.form['game_id'])
    i = session_game.game
    print(i)
    print(i[int(request.form['button_id'])])
    print(int(request.form['button_id']))
    game_id = request.form['game_id']
    print(session_game.status, 'статус')
    if i[int(request.form['button_id'])] == '1' and session_game.status == '0':
        session_game.status = 'lose'
        db.session.commit()
        return jsonify({'data': int(1)})
    elif session_game.status == '0':
        status_num += 1
        if len(i) == 4 and session_game.status == '0':
            status_num = 0
            session_game.status = 'win'
            db.session.commit()
            return jsonify({'data': int(0), 'status': int(1)})
        elif len(i) == 9 and status_num == 3 and session_game.status == '0':
            status_num = 0
            session_game.status = 'win'
            db.session.commit()
            return jsonify({'data': int(0), 'status': int(1)})
        elif len(i) == 16 and status_num == 5 and session_game.status == '0':
            status_num = 0
            session_game.status = 'win'
            db.session.commit()
            return jsonify({'data': int(0), 'status': int(1)})
        print(status_num)
        return jsonify({'data': int(0), 'status': int(0)})


if __name__ == '__main__':
    app.run()
