from app import create_app
from app.models.base import db
from app.models.user import User

app = create_app()
with app.app_context():     #把app推入到上下文栈中去才能调用db.create_all让它生效
    with db.auto_commit():
        # 创建一个超级管理员
        user = User()
        user.nickname = 'Super'
        user.password = '123456'
        user.email = '999@qq.com'
        user.auth = 2
        db.session.add(user)
