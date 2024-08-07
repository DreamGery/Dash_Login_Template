import datetime

import dash
from flask_jwt_extended import JWTManager
from flask_login import LoginManager, UserMixin

from models.model import Auth

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,  # 避免出现组件ID不存在的报错
    update_title=None,
)

# 获取flask实例
server = app.server

# 初始化登陆管理类以及JWT
login_manager = LoginManager()
jwt = JWTManager(server)

login_manager.login_view = "/"

# 配置密钥 密钥建议不要明文显示在代码中
server.secret_key = "DreamGery"
server.config["JWT_SECRET_KEY"] = "DreamGery"

# 配置用户登录状态有效期
server.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=7)

# 配置jwt有效期
server.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(hours=1)

# 配置refresh token有效期
server.config['JWT_REFRESH_TOKEN_EXPIRES'] = datetime.timedelta(days=7)

# 配置JWT令牌存储在cookies
server.config['JWT_TOKEN_LOCATION'] = ['cookies']

# 设置cookies名称
server.config['JWT_COOKIE_NAME'] = 'dash_access_token'

# 绑定纳入鉴权范围的flask实例
login_manager.init_app(server)

class User(UserMixin):
    pass

@login_manager.user_loader
def load_uesr(username):
    auth = Auth()
    user_information = auth.return_user_information(username=username)
    
    current_user = User()
    current_user.username = user_information.username
    current_user.role = user_information.user_role

    return current_user

if __name__ == "__main__":
    user = load_uesr(username='DreamGery')
