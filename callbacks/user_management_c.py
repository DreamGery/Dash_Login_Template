import dash
import feffery_antd_components as fac
from flask_login import current_user
from dash.dependencies import Input, Output, State

from models.model import auth
from server import app


@app.callback(
    [
        Output('user-table', 'data'),
        Output('user-information-message-container', 'children', allow_duplicate=True)
    ],
    Input('popconfirm-delete-user', 'confirmCounts'),
    State('user-table', 'selectedRows'),
    prevent_initial_call=True
)
def delete_user(confirmCounts, selectedRows):
    if '用户管理' not in auth.return_user_information(current_user.username).user_permission.get('permisssion'):
        return dash.no_update

    if confirmCounts:
        if selectedRows:

            # 避免删除了超级管理员的账号
            delete_username = [
                i.get('username') for i in selectedRows if i.get('user_role') != '超级管理员'
            ]
            delete_user_message =  auth.delete_user(username=delete_username)
            if delete_user_message['status'] == 'success':
                return [
                    auth.return_user_table().to_dict('records'),
                    fac.AntdMessage(content='删除成功', type='success')
                ]
            else:
                return [
                    dash.no_update,
                    fac.AntdMessage(content='删除失败', type='error')
                ]
        else:
            return [dash.no_update, fac.AntdMessage(content='未选择需要删除的用户', type='warning')]
    else:
        return [dash.no_update, None]
        


