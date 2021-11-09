from flask import Flask, flash, jsonify
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from game import GameTwo, GameThree, GameFour, UnicNum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Register(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bet = db.Column(db.String(300), nullable=False)
    game = db.Column(db.String(300), nullable=False)
    status = db.Column(db.String(300), nullable=True)
    cards_open = db.Column(db.String(300), nullable=True)
    cash = db.Column(db.String(300), nullable=True)


@app.route('/', methods=['POST', 'GET'])
def main():
    cash = Register.query.get(1)
    if request.method == "POST":
        if request.form['game'] == '2':
            bet = request.form['bet']
            game_num = GameTwo()
            print('создание игры')
            new_game = Register(bet=bet, game=game_num, status=0, cards_open='')
            try:
                db.session.add(new_game)
                db.session.commit()
                game_id = db.session.query(Register).order_by(Register.id)[-1]
            except:
                return "Ошибка сохранения"
            return render_template('gameTwo.html', game_id=game_id, cash=cash.cash)  # добавить айди нового пользователя
        elif request.form['game'] == '3':
            bet = request.form['bet']
            game_num = GameThree()
            new_game = Register(bet=bet, game=game_num, status=0, cards_open='')
            try:
                db.session.add(new_game)
                db.session.commit()
                game_id = db.session.query(Register).order_by(Register.id)[-1]
            except:
                return "Ошибка сохранения"
            return render_template('gameThree.html', game_id=game_id, cash=cash.cash)
        elif request.form['game'] == '4':
            bet = request.form['bet']
            game_num = GameFour()
            new_game = Register(bet=bet, game=game_num, status=0, cards_open='')
            try:
                db.session.add(new_game)
                db.session.commit()
                game_id = db.session.query(Register).order_by(Register.id)[-1]
            except:
                return "Ошибка сохранения"
            return render_template('gameFour.html', game_id=game_id, cash=cash.cash)
        else:
            pass

    return render_template('index.html', cash=cash.cash)


@app.route('/lose', methods=['GET'])
def lose():
    return render_template('Lose.html', game_id=1)


@app.route('/update', methods=['POST', 'GET'])
def updateNum():
    session_game = Register.query.get(request.form['game_id'])
    cash = Register.query.get(1)
    i = session_game.game
    if session_game.status == '0':
        if len(i) == 4:
            session_game.cards_open += i[int(request.form['button_id'])]
            db.session.commit()
            print(session_game.cards_open, 'открытые карты')
            if len(session_game.cards_open) == 2 and session_game.cards_open[0] == session_game.cards_open[
                1] and session_game.status == '0':
                session_game.status = 'win'
                db.session.commit()
                pic_num = i[int(request.form['button_id'])]
                money = int(cash.cash)
                money += int(session_game.bet) * 2
                cash.cash = money
                db.session.commit()
                return jsonify({'data': pic_num, 'game': 1, 'cash': cash.cash})
            elif len(session_game.cards_open) == 2 and session_game.cards_open[0] != session_game.cards_open[
                1] and session_game.status == '0':
                session_game.status = 'lose'
                db.session.commit()
                pic_num = i[int(request.form['button_id'])]
                return jsonify({'data': pic_num, 'game': 0, 'cash': cash.cash})
            pic_num = i[int(request.form['button_id'])]
            return jsonify({'data': pic_num, 'game': 3, 'cash': cash.cash})
        elif len(i) == 9:
            session_game.cards_open += i[int(request.form['button_id'])]
            db.session.commit()
            print(len(session_game.cards_open), 'открытые карты')
            if len(session_game.cards_open) == 4 and UnicNum(session_game.cards_open, 3) == '1' \
                    and session_game.status == '0':
                session_game.status = 'win'
                db.session.commit()
                pic_num = i[int(request.form['button_id'])]
                money = int(cash.cash)
                money += int(session_game.bet) * 3
                cash.cash = money
                db.session.commit()
                return jsonify({'data': pic_num, 'game': 1, 'cash': cash.cash})
            elif len(session_game.cards_open) == 4 and UnicNum(session_game.cards_open, 3) == '0' \
                    and session_game.status == '0':
                session_game.status = 'lose'
                db.session.commit()
                pic_num = i[int(request.form['button_id'])]
                return jsonify({'data': pic_num, 'game': 0, 'cash': cash.cash})
            pic_num = i[int(request.form['button_id'])]
            return jsonify({'data': pic_num, 'game': 3, 'cash': cash.cash})
        elif len(i) == 16:
            session_game.cards_open += i[int(request.form['button_id'])]
            db.session.commit()
            print(len(session_game.cards_open), 'открытые карты')
            if len(session_game.cards_open) == 6 and UnicNum(session_game.cards_open, 4) == '1' \
                    and session_game.status == '0':
                print(1)
                session_game.status = 'win'
                db.session.commit()
                pic_num = i[int(request.form['button_id'])]
                money = int(cash.cash)
                money += int(session_game.bet) * 4
                cash.cash = money
                db.session.commit()
                return jsonify({'data': pic_num, 'game': 1, 'cash': cash.cash})
            elif len(session_game.cards_open) == 6 and UnicNum(session_game.cards_open, 4) == '0' \
                    and session_game.status == '0':
                print(2)
                session_game.status = 'lose'
                db.session.commit()
                pic_num = i[int(request.form['button_id'])]
                return jsonify({'data': pic_num, 'game': 0, 'cash': cash.cash})
            pic_num = i[int(request.form['button_id'])]
            return jsonify({'data': pic_num, 'game': 3, 'cash': cash.cash})


if __name__ == '__main__':
    app.run()


