from main import db, User
from datetime import datetime

user = {'farmname': 'farm2', 'coordinates': '42.6334, 71.3162', 'farmtype': 'pesticide', 'about': 'good farm', 'username': 'bruh', 'password': 'hello', 'date': datetime.now()}


def addFarm():
    farm = User(farmname=user['farmname'], address=user['coordinates'], farmtype=user['farmtype'], about=user['about'], username=user['username'], password=user['password'], date_created=user['date'])
    db.session.add(farm)
    db.session.commit() 



farms = db.session.query(User).all()
print(farms[1].id)