import dash
import feffery_utils_components as fuc
from dash import dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from flask_login import current_user
from flask_jwt_extended import create_access_token, decode_token

import views
from config import RouterConfig
from server import app
from models.model import auth

app.layout = html.Div(
    [
        # 注入url监听
        fuc.FefferyLocation(id="url"),

        # 注入页面内容挂载点
        html.Div(id="app-mount"),

        # 路由重定向
        html.Div(id="router-redirect-container"),

        # 注入消息提示容器
        html.Div(
            [
                # "用户管理-新增用户"消息提示
                html.Div(id="index-user-manage-add-user-message-container"),
            ]
        ),

        # 注入cookies组件
        fuc.FefferyCookie(
            id='jwt-cookies',
            cookieKey='dash_access_token'
        ),
    ]
)


@app.callback(
    [
        Output("app-mount", "children", allow_duplicate=True), 
        Output("router-redirect-container", "children", allow_duplicate=True)
    ],
    Input("url", "pathname"),
    State('url', 'trigger'),
    prevent_initial_call=True
)
def router(pathname, trigger):
    # 检验pathname合法性
    if pathname not in RouterConfig.VALID_PATHNAME:
        # 渲染404状态页
        return [
            views._404.render_404_content(),
            None
        ]

    # 检查当前会话是否已经登录
    # 若已登录
    if current_user.is_authenticated:
        # 根据pathname控制渲染行为
        if pathname == '/login':
            # 重定向到主页面
            return [
                dash.no_update,
                dcc.Location(
                    pathname='/',
                    id='router-redirect'
                )
            ]
        elif trigger == 'pushstate':
            return dash.no_update
        else:
            return [
                views.index.render_index_content(
                    username=current_user.username,
                    permission=(
                        auth
                        .return_user_information(current_user.username)
                        .user_permission
                        .get('permission')
                    )
                ),
                None
            ]
            

    # 若未登录
    # 根据pathname控制渲染行为
    if pathname == '/login':
        return [
            views.login.render_login_content(),
            []
        ]
    else:
        # 否则重定向到登录页
        return [
            dash.no_update,
            dcc.Location(
                pathname='/login',
                id='router-redirect'
            )
        ]

@app.callback(
    Output('jwt-cookies', 'value', allow_duplicate=True),
    Input('url', 'trigger'),
    prevent_initial_call=True
)
def get_new_access_token(trigger):
    if current_user.is_authenticated and trigger == 'load':
        refresh_token = auth.return_user_information(username=current_user.username).refresh_toekn
        try:
            decode_token(encoded_token=refresh_token)
            return create_access_token(identity=current_user.username)
        except Exception:
            raise PreventUpdate
    else:
        raise PreventUpdate



if __name__ == "__main__":
    app.run_server(debug=True)