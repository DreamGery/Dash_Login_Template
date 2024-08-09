import dash
import feffery_antd_components as fac
from flask_login import current_user
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from config import RouterConfig
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
    # 避免知道路由能够直接访问
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
        
@app.callback(
    Output('modal-container', 'children', allow_duplicate=True),
    Input('add-user-button', 'nClicks'),
    prevent_initial_call=True
)
def add_user_modal(nClicks):
    if nClicks:
        return fac.AntdModal(
            [
                fac.AntdForm(
                    [
                        fac.AntdFormItem(fac.AntdInput(id='add-username-input'), label='用户名'),
                        fac.AntdFormItem(fac.AntdInput(value='DreamGery', disabled=True, id='add-user-password'), label='默认密码'),
                        fac.AntdFormItem(
                            fac.AntdSelect(
                                id='user-role-select',
                                options=['普通用户', '超级管理员']
                            ),
                            label='用户角色'
                        ),
                        fac.AntdFormItem(
                            fac.AntdSelect(
                                id='add-user-permission-select',
                                options=RouterConfig.NORMAL_PERMISSION,
                                mode='multiple'
                            ),
                            label='用户权限',
                            tooltip='普通用户默认有个人信息权限, 超级管理员默认有用户管理权限'
                        )
                    ],
                    id='add-user-form',
                    enableBatchControl=True
                )
            ],
            renderFooter=True,
            visible=True,
            id='add-user-modal',
            title='增加用户'
        )
    else:
        raise PreventUpdate

@app.callback(
    [
        Output('user-table', 'data', allow_duplicate=True),
        Output('user-information-message-container', 'children', allow_duplicate=True)
    ],
    Input('add-user-modal', 'okCounts'),
    [
        State('add-user-form', 'values')
    ],
    prevent_initial_call=True
)
def add_user_function(okCounts, values):
    if okCounts and values:
        if len(values) == 5:
            if auth.add_user(
                username=values.get('add-username-input'),
                password=values.get('add-user-password'),
                user_role=values.get('user-role-select'),
                user_permission={'permission': values.get('add-user-permission-select')}
            ):
                return 

    else:
        raise PreventUpdate