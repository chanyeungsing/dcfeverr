from app import db, app
from app.models import User, Post, News


app_context = app.app_context()
app_context.push()
db.drop_all()
db.create_all()

u1 = User(username='john', email='john@example.com',about_me="i am john")
u2 = User(username='susan', email='susan@example.com',about_me="i am susan")
u1.set_password("P@ssw0rd")
u2.set_password("P@ssw0rd")
db.session.add(u1)
db.session.add(u2)
u1.follow(u2)
u2.follow(u1)

p1 = Post(body='my first post!', author=u1)
p2 = Post(body='my first post!', author=u2)
db.session.add(p1)
db.session.add(p2)

news1 = News(title="new1",content="There is a news.")
news2 = News(title="new2",content="There is a news.")
db.session.add(news1)
db.session.add(news2)

db.session.commit()
