from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Configuration  # импорт конфигурации

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)


from database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
