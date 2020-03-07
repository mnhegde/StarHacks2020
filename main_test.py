from main import db, User
from datetime import datetime

user = {'farmname': 'Fresh Farm', 'coordinates': '32.6334, 70.3162', 'farmtype': 'Organic', 'about': 'Fresh produce', 'username': 'bruh', 'password': 'hello', 'date': datetime.now()}


def addFarm():
    farm = User(farmname=user['farmname'], address=user['coordinates'], farmtype=user['farmtype'], about=user['about'], username=user['username'], password=user['password'], date_created=user['date'])
    db.session.add(farm)
    db.session.commit() 

addFarm()


farms = db.session.query(User).all()
print(farms[-1].id)