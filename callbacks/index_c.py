import dash
import feffery_antd_components as fac
from dash import dcc
from dash.dependencies import Input, Output
from flask_jwt_extended import create_access_token, decode_token, jwt_required
from flask_login import current_user, logout_user

from config import RouterConfig
from models.model import auth
from server import app
from views.forbidden_access import render_access_content
from views.personal_information import render_user_page_content
from views.user_management import render_user_management_content
from views.dashboard import render_dashboard_content


# 控制header的样式
app.clientside_callback(
    '''
    (position, state) => {
        if (position) {
            if (position.top > 0) {
                return {
                    'backgroundColor': 'transparent',
                    'height': '64px',
                    'backdropFilter': 'blur(10px)',
                    'borderBlockEnd': '1px solid rgba(5, 5, 5, 0.06)',
                    'transition': 'background-color 1s ease'
                };
            } else {
                return {
                    'backgroundColor': (state === 'dark' ? '#001529' : 'rgba(255, 255, 255, 1)'),
                    'height': '64px',
                    'backdropFilter': 'blur(10px)',
                    'borderBlockEnd': '1px solid rgba(5, 5, 5, 0.06)',
                    'transition': 'background-color 1s ease'
                };
            }
        } else {
            return {
                'height': '64px',
                'backdropFilter': 'blur(10px)',
                'borderBlockEnd': '1px solid rgba(5, 5, 5, 0.06)',
                'transition': 'background-color 1s ease'
            };
        }
    }
    ''',
    Output('header', 'style'),
    [
        Input('scroll-listener', 'position'),
        Input('config', 'algorithm')
    ]
)

# 监听浏览器断点, 来控制menu的缩略形态
app.clientside_callback(
    '''
    (responsive) => {
        if (responsive) {
            if (!responsive.lg) {
                return 0
            } 
            else {
                return 80
            }
        } 
        else {
            window.dash_clientside.no_update
        }
    }
    ''',
    Output('antd-sider', 'collapsedWidth'),
    Input('breakpoint-listener', 'responsive')
)

# 是否切换暗黑模式
app.clientside_callback(
    '''
    (checked) => {
        if (checked) {
            return 'dark'
        }
        else {
            return 'default'
        }
    }
    ''',
    Output('config', 'algorithm'),
    Input('mode', 'checked')
)

app.clientside_callback(
    '''
    (pathname) => {
        let menuItem = {
            '/user-management': '用户管理'
        }
        return menuItem[pathname]
    }
    ''',
    Output('menu', 'currentKey'),
    Input('url', 'pathname')
)

@app.callback(
    [
        Output('router-redirect-container', 'children'),
        Output('jwt-cookies', 'value', allow_duplicate=True)
    ],
    Input('header-dropdown-menu', 'clickedKey'),
    prevent_initial_call=True
)
def logout_callback(clickedKey):
    if clickedKey == 'logout':
        logout_user()
        return [
            dcc.Location(id='router-redirect', pathname='/login'), 
            'None' #治标不治本，因为单纯就是把客户端的token给去除，token还是有效的，后期采用redis等手段弄一个黑名单
        ]
    else:
        return dash.no_update

@jwt_required()
@app.callback(
    Output('content-container', 'children'),
    Input('url', 'pathname')
)
def render_content(pathname):
    if pathname == '/':
        return fac.AntdNotification(
            type='warning',
            message='请在左边菜单栏选择页面'
        )
    
    if RouterConfig.PATHNAME_PERMISSION.get(pathname) not in (
        auth.return_user_information(current_user.username).user_permission.get('permission')
    ):
        return render_access_content()
    content_dict = {
        '/user-management': render_user_management_content(user_data=auth.return_user_table()),
        '/user-information': render_user_page_content(user_information=auth.return_user_information(username=current_user.username)),
        '/dashboard': render_dashboard_content()
    }

    return content_dict.get(pathname, None)

# 刷新jwt令牌 45分钟一次
@app.callback(
    Output('jwt-cookies', 'value', allow_duplicate=True),
    Input('jwt-interval', 'n_intervals'),
    prevent_initial_call=True
)
def refresh_access_token(n_intervals):
    if current_user.is_authenticated and n_intervals:
        refresh_token = auth.return_user_information(username=current_user.username).refresh_token
        
        try:
            decode_token(encoded_token=refresh_token)
            return create_access_token(identity=current_user.username)
        except Exception:
            return dash.no_update

    else:
        return dash.no_update