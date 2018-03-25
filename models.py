from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import mapper
from database import db_session, metadata


class User(object):
    query = db_session.query_property()

    def __init__(self, date=None, ip=None, funcn=None, value1=None, value2=None, result=None):
        self.date = date
        self.ip = ip
        self.funcn = funcn
        self.value1 = value1
        self.value2 = value2
        self.result = result

    def __repr__(self):
        return '<Date %r | IP %r  | Func %r  | Value1 %r | Value2 %r | Result %r>' % (self.date, self.ip, self.funcn, self.value1, self.value2, self.result)


users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('date', String(100)),
              Column('ip', String(50)),
              Column('funcn', String(50)),
              Column('value1', String(50)),
              Column('value2', String(50)),
              Column('result', String(50)),
              )
mapper(User, users)
