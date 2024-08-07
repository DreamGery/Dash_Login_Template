import time

import dash
from dash import Input, Output, State, dcc
from flask_login import login_user
from flask_jwt_extended import create_access_token, create_refresh_token

from models.model import auth
from server import User, app


@app.callback(
    Output('tabs', 'style'),
    Input('url', 'pathname')
)
def tab_animation(pathname):
    if pathname == '/login':
        time.sleep(0.5)
        return {}
    else:
        return dash.no_update
    
@app.callback(
    [
        Output('form-item-username', 'validateStatus'),
        Output('form-item-username', 'help'),
        Output('form-item-password', 'validateStatus'),
        Output('form-item-password', 'help'),
        Output('router-redirect-container', 'children', allow_duplicate=True),
        Output('jwt-cookies', 'value')
    ],
    Input('login-submit', 'nClicks'),
    [
        State('username-input', 'value'),
        State('password-input', 'md5Value'),
        State('remember', 'checked')
    ],
    prevent_initial_call=True
)
def login(nClicks, value, md5Value, checked):
    """
    登录逻辑

    参数:
        nClicks (int): 单纯用来判断登录按钮有没有被点击
        value (str): 账号
        md5Value (str): md5加密后的密码
        checked (bool): 是否保持登录(有效期默认7天)
    """
    if nClicks:
        if auth.check_users_name(username=value).get('status') == 'exist':
            if auth.check_password(username=value, password=md5Value).get('status') == 'success':
                current_user = User()
                current_user.id = value
                login_user(current_user, remember=checked)
                access_token = create_access_token(identity=value)
                refresh_token = create_refresh_token(identity=value)
                auth.change_user_information(username=value, changed_data={'refresh_token': refresh_token})
                return [
                    None,
                    None,
                    None,
                    None,
                    dcc.Location(pathname='/', id='router-redirect'),
                    access_token
                ]
            else:
                return [None, None, 'error', '密码错误', None, dash.no_update]
        else:
            return ['error', '账号错误', None, None, None, dash.no_update]
    else:
        return dash.no_update