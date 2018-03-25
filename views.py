from app import app
from flask import request, jsonify
import socket

from database import init_db, db_session
from models import User

from datetime import datetime, date

@app.route('/')
def homepage():
    return "home page"


@app.route('/mult', methods=['POST'])
def mult():
    data = request.get_json()
    value1 = data['v1']
    value2 = data['v2']
    res = int(value1) * int(value2)

    #work with database
    init_db()
    d_today = datetime.now()
    dd = d_today.date()
    ss = socket.gethostbyname(socket.gethostname())
    u = User(str(dd), str(ss), str(1), value1, value2, str(res))
    db_session.add(u)
    db_session.commit()

    return jsonify({'mult': res})

@app.route('/div', methods=['POST'])
def div():
    data = request.get_json()
    value1 = data['v1']
    value2 = data['v2']
    res = int(value1) / int(value2)

    #work with database
    init_db()
    d_today = datetime.now()
    dd = d_today.date()
    ss = socket.gethostbyname(socket.gethostname())
    u = User(str(dd), str(ss), str(2), value1, value2, str(res))
    db_session.add(u)
    db_session.commit()

    return jsonify({'div': res})

@app.route('/sum', methods=['POST'])
def sum():
    data = request.get_json()
    value1 = data['v1']
    value2 = data['v2']
    res = int(value1) + int(value2)

    #work with database
    init_db()
    d_today = datetime.now()
    dd = d_today.date()
    ss = socket.gethostbyname(socket.gethostname())
    u = User(str(dd), str(ss), str(3), value1, value2, str(res))
    db_session.add(u)
    db_session.commit()

    return jsonify({'sum': res})

@app.route('/pos', methods=['POST'])
def pos():
    data = request.get_json()
    value1 = data['v1']
    value2 = data['v2']
    res = int(value1) ** int(value2)

    #work with database
    init_db()
    d_today = datetime.now()
    dd = d_today.date()
    ss = socket.gethostbyname(socket.gethostname())
    u = User(str(dd), str(ss), str(4), value1, value2, str(res))
    db_session.add(u)
    db_session.commit()

    return jsonify({'pos': res})

@app.route('/logs', methods=['GET'])
def logs():
    return str(User.query.all())


@app.route('/report', methods=['GET', 'POST'])
def report_day():
    if request.method == 'GET':
        sum_v = User.query.filter(User.funcn == '3').count()
        mult_v = User.query.filter(User.funcn == '1').count()
        div_v = User.query.filter(User.funcn == '2').count()
        pos_v = User.query.filter(User.funcn == '4').count()
    else:
        data_date = request.get_json()
        dd = data_date['date']

        sum_v = User.query.filter(User.date == dd, User.funcn == '3').count()
        mult_v = User.query.filter(User.date == dd, User.funcn == '1').count()
        div_v = User.query.filter(User.date == dd, User.funcn == '2').count()
        pos_v = User.query.filter(User.date == dd, User.funcn == '4').count()

    return jsonify({'Возведение в степень': pos_v, 'Деление': div_v, 'Умножение': mult_v, 'Сложение': sum_v})