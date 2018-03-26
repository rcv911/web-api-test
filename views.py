from sqlalchemy import func

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
    dd = datetime.now()
    # dd = d_today.date()
    ss = request.remote_addr
    u = User(str(dd), ss, 'Умножение', value1, value2, str(res))
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
    dd = datetime.now()
    # dd = d_today.date()
    ss = request.remote_addr
    u = User(str(dd), ss, 'Деление', value1, value2, str(res))
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
    dd = datetime.now()
    # dd = d_today.date()
    ss = request.remote_addr
    u = User(str(dd), ss, 'Сумма', value1, value2, str(res))
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
    dd = datetime.now()
    # dd = d_today.date()
    ss = request.remote_addr
    u = User(str(dd), ss, 'Возведение в степень', value1, value2, str(res))
    db_session.add(u)
    db_session.commit()

    return jsonify({'pos': res})

@app.route('/logs', methods=['GET'])
def logs():
    return str(User.query.all())

@app.route('/group', methods=['GET', 'POST'])
def group():
    if request.method == 'GET':
        lst = db_session.query(User.funcn, func.count()).group_by(User.funcn).all()
    else:
        data_date = request.get_json()
        dd = data_date['date']
        lst = db_session.query(User.funcn, func.count()).filter(User.date.like("%"+str(dd)+"%")).group_by(User.funcn).all()
        if lst == []:
            lst = 'Запросов не было'

    return jsonify({'Отчет: ': lst})


@app.route('/report', methods=['GET', 'POST'])
def report_day():
    if request.method == 'GET':
        sum_v = User.query.filter(User.funcn == 'Сумма').count()
        mult_v = User.query.filter(User.funcn == 'Умножение').count()
        div_v = User.query.filter(User.funcn == 'Деление').count()
        pos_v = User.query.filter(User.funcn == 'Возведение в степень').count()
    else:
        data_date = request.get_json()
        dd = data_date['date']

        sum_v = User.query.filter(User.date.like("%"+str(dd)+"%"), User.funcn == 'Сумма').count()
        mult_v = User.query.filter(User.date.like("%"+str(dd)+"%"), User.funcn == 'Умножение').count()
        div_v = User.query.filter(User.date.like("%"+str(dd)+"%"), User.funcn == 'Деление').count()
        pos_v = User.query.filter(User.date.like("%"+str(dd)+"%"), User.funcn == 'Возведение в степень').count()

    return jsonify({'Возведение в степень': pos_v, 'Деление': div_v, 'Умножение': mult_v, 'Сложение': sum_v})


# @app.route("/ip", methods=["GET"])
# def ip():
#     return request.environ