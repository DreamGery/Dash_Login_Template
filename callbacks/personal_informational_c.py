import dash
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State
from flask_jwt_extended import jwt_required
from flask_login import current_user

from models.model import auth, is_authorized
from server import app


@app.callback(
    [
        Output('old-password', 'value'),
        Output('new-password', 'value'),
        Output('confirm-new-password', 'value'),
        Output('user-page-message-container', 'children')
    ],
    Input('submit-new-password', 'nClicks'),
    [
        State('old-password', 'md5Value'),
        State('new-password', 'md5Value'),
        State('confirm-new-password', 'md5Value'),
    ]
)
@is_authorized(user=current_user, view='个人信息')
@jwt_required()
def update_password(nClicks, old_password, new_pass_word, confirm_new_password):
    # if '个人信息' not in auth.return_user_information(current_user.username).user_permission.get('permission'):
    #     return dash.no_update

    if nClicks:
        if all([old_password, new_pass_word, confirm_new_password]):
            db_old_password = auth.return_user_information(current_user.username).password

            if old_password != db_old_password:
                return [
                    None,
                    dash.no_update,
                    dash.no_update,
                    fac.AntdMessage(
                        content='原密码错误',
                        type='warning'
                    )
                ]
            
            if new_pass_word != confirm_new_password:
                return [
                    dash.no_update,
                    None,
                    None,
                    fac.AntdMessage(
                        content='二次输入的新密码与第一次输入的不一致'
                    )
                ]
            
            if auth.change_user_information(
                username=current_user.username,
                changed_data={
                    'password': confirm_new_password
                }
            ).get('status') == 'success':
                return [
                    None,
                    None,
                    None,
                    fac.AntdMessage(
                        content='修改成功',
                        type='success'
                    )
                ]
            else:
                return [
                    dash.no_update,
                    dash.no_update,
                    dash.no_update,
                    fac.AntdMessage(
                        content='修改失败',
                        type='warning'
                    )
                ]
        else:
            return [
                dash.no_update,
                dash.no_update,
                dash.no_update,
                fac.AntdMessage(
                    content='请补全信息',
                    type='error'
                )
            ]
    else:
        return dash.no_update