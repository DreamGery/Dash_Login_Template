import feffery_antd_components as fac

from dash import html

from models.model import Auth
from callbacks import user_management_c  # noqa: F401

def render_user_management_content(user_data=Auth().return_user_table()):
    content = fac.AntdCenter(
        [
            fac.AntdCard(
                [
                    fac.AntdRow(
                        fac.AntdCol(
                            fac.AntdSpace(
                                [
                                    fac.AntdButton(
                                        "新增用户", 
                                        type="primary",
                                        id='add-user-button'
                                    ),
                                    fac.AntdPopconfirm(
                                        fac.AntdButton(
                                            "删除用户", 
                                            type="primary", 
                                            danger=True,
                                            id='delete-user-button'
                                        ),
                                        title='确认继续删除',
                                        id='popconfirm-delete-user'
                                    ),
                                    fac.AntdButton(
                                        "修改用户信息",
                                        id='update-user-button'
                                    ),
                                ]
                            )
                        ),
                        style={
                            'marginBottom': '20px'
                        }
                    ),
                    fac.AntdRow(
                        fac.AntdCol(
                            fac.AntdTable(
                                data=user_data.to_dict('records'),
                                columns=[
                                    {
                                        "title": "用户名", 
                                        "dataIndex": "username"
                                    },
                                    {
                                        "title": "角色", 
                                        "dataIndex": "user_role"
                                    },
                                    {
                                        "title": "用户权限", 
                                        "dataIndex": "permission",
                                        "renderOptions": {"renderType": "tags"}
                                    },
                                ],
                                rowSelectionType='checkbox',
                                id='user-table'
                            ),
                            span=24
                        ),
                        style={
                            'width': '100%'
                        }
                    ),
                    html.Div(id='user-information-message-container'),
                    html.Div(id='modal-container')
                ],
                hoverable=True,
                headStyle={
                    "display": 'none',
                },
                style={
                    'width': '60%',
                    'height': '65%'
                }
            )
        ],
        style={
            "width": "100%", 
            "height": "100%"
        },
    )

    return content



