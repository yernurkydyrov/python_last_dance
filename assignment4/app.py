from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import text
from sqlalchemy import create_engine

app = Flask(__name__, template_folder='templates/')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:hashirama@localhost/pythonassignment4'
db = SQLAlchemy(app)

engine = create_engine('postgresql://postgres:hashirama@localhost/pythonassignment4')


class News(db.Model):
    __table__ = 'news'
    id_coin = db.Column('coin_id', db.Integer, primary_key=True)
    coin_name = db.Column('coin_name', db.Unicode)
    news1 = db.Column('news1', db.Unicode)
    news2 = db.Column('news2', db.Unicode)
    news3 = db.Column('news3', db.Unicode)
    news4 = db.Column('news4', db.Unicode)
    news5 = db.Column('news5', db.Unicode)
    news6 = db.Column('news6', db.Unicode)
    news7 = db.Column('news7', db.Unicode)
    news8 = db.Column('news8', db.Unicode)
    news9 = db.Column('news9', db.Unicode)
    news10 = db.Column('news10', db.Unicode)
    news11 = db.Column('news11', db.Unicode)
    news12 = db.Column('news12', db.Unicode)
    news13 = db.Column('news13', db.Unicode)
    news14 = db.Column('news14', db.Unicode)
    news15 = db.Column('news15', db.Unicode)
    news16 = db.Column('news16', db.Unicode)
    news17 = db.Column('news17', db.Unicode)
    news18 = db.Column('news18', db.Unicode)
    news19 = db.Column('news19', db.Unicode)
    news20 = db.Column('news20', db.Unicode)

    def __init__(self, id_coin: object, coin_name: object, news1: object, news2: object, news3: object, news4: object, news5: object, news6: object, news7: object, news8: object, news9: object,
                 news10: object,
                 news11: object,
                 news12: object, news13: object, news14: object, news15: object, news16: object, news17: object, news18: object, news19: object, news20: object) -> object:
        self.id_coin = id_coin
        self.coin_name = coin_name
        self.news1 = news1
        self.news2 = news2
        self.news3 = news3
        self.news4 = news4
        self.news5 = news5
        self.news6 = news6
        self.news6 = news7
        self.news8 = news8
        self.news9 = news9
        self.news10 = news10
        self.news11 = news11
        self.news12 = news12
        self.news13 = news13
        self.news14 = news14
        self.news15 = news15
        self.news16 = news16
        self.news17 = news17
        self.news18 = news18
        self.news19 = news19
        self.news20 = news20
