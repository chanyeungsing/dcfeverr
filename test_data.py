from app import db, app
from app.models import User, Post, News, Camera


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

news1 = News(title="Tesla 或有望再減價？Elon Musk 直言接受「零淨利」",content="""Tesla 近來的減價促銷策略，確實讓旗下電動車的銷售量有所提升。可是，作為短期促銷是可以，卻總不能長期維持吧？不過 Tesla 行政總裁 Elon Musk 早前卻表示，Tesla 不僅願意在短期內通過犧牲獲利以追求銷售量，甚至更可以接受「零淨利」！難度這表示 Tesla 還有機會進一步減價？根據 Tesla 公布的第一季財務報告顯示，減價促銷這一招確實有助提升消費者購買意慾，亦能夠為公司利潤獲得增長。不過最讓人驚訝的是，Elon Musk 直言樂意繼續利用減價來提升銷售量，而他更表明追求更多的銷售數字，才是正確的發展方向。為何 Elon Musk 能夠放出如此豪言壯語？Tesla 透過減價提升銷量，但是他們的收入不單止是賣車，軟體升級也是他們的收入來源之一，而且佔比相當重要，這亦是 Elon Musk 如此敢於說出願意接受「零淨利」的原因。Tesla 較早前透露，將會再推出一款定位上更平民的車款，成本比 Model Y 便宜一半。如果 Tesla 真的有進一步減價空間，大家會否再等呢？""",imgurl="https://cdn01.dcfever.com/articles/news/2023/04/20230426_tesla_01.jpg")
news2 = News(title="Sony Xperia 1 V 五月發佈：小編收風可當 Xperia Pro I II",content=""" 市場上  Asus﹑Honor﹑Samsung 及小米等都先後推出 2023 年的旗艦手機，Sony 有傳亦緊隨其後，將會在 5 月份公佈新一代旗艦機 Xperia 1 V。據消息指 Sony 會於 5 月 24 日中國舉行的 Sony Expo 2023 活動中發表 Xperia 1 V。與去年 Sony 在 5 月初發佈 Xperia 1 IV，一年後發佈新一代旗艦機，時間上亦十分吻合。小編據知情人士透露，Sony Xperia 1 V 攝力將有不少提升，用家可當 Xperia Pro I-II 看待，因為 Xperia Pro 系列，據了解今年推出新機的機會不大，要等 Xperia Pro I 後繼機的朋友，可以安心地購買 Xperia 1 V。""",imgurl="https://cdn01.dcfever.com/articles/news/2023/04/220427_sonyexpo_01.jpg")
db.session.add(news1)
db.session.add(news2)

camera1 = Camera(brand="Fujifilm", model="Fujifilm X100V",price=10999,total_score=5,imgurl="https://cdn09.dcfever.com/media/cameras//images/2020/02/fujifilm_2367_1580878671.jpg")
camera2 = Camera(brand="Canon", model="Canon EOS R8",price=1380,total_score=5,imgurl="https://cdn09.dcfever.com/media/cameras//images/2023/02/canon_2441_1675844868.jpg")
db.session.add(camera1)
db.session.add(camera2)

db.session.commit()
