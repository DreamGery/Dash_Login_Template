import dash
import feffery_antd_components as fac

from dash import html
from callbacks import personal_informational_c

def render_user_page_content(user_information):

    content = fac.AntdCenter(
        [
            fac.AntdTabs(
                items=[
                    {
                        "key": "基本信息",
                        "label": "基本信息",
                        "children": fac.AntdCard(
                            [
                                fac.AntdCardMeta(
                                    avatar=fac.AntdAvatar(size="large"),
                                    title="用户信息",
                                    description=[
                                        fac.AntdForm(
                                            [
                                                # fac.AntdFormItem(
                                                    # fac.AntdUpload(
                                                        # buttonContent="点击更改头像",
                                                        # fileTypes=["jpg", "jpeg", "png"],
                                                    # ),
                                                # ),
                                                fac.AntdFormItem(
                                                    fac.AntdSpace(
                                                        [
                                                            fac.AntdInput(value=user_information.username),
                                                            # fac.AntdButton(
                                                                # "确认修改", type="primary"
                                                            # ),
                                                        ]
                                                    ),
                                                    label="昵称",
                                                ),
                                                fac.AntdFormItem(
                                                    fac.AntdSelect(
                                                        options=[],
                                                        value=user_information.user_permission.get('permission'),
                                                        readOnly=True,
                                                        mode="multiple",
                                                        disabled=True,
                                                    ),
                                                    label="权限",
                                                ),
                                            ],
                                            layout="vertical",
                                            style={"height": "100%", 'width': '100%'},
                                        )
                                    ],
                                )
                            ],
                            style={"width": "75%", "height": "100%"},
                            bordered=False,
                            hoverable=True,
                            headStyle={"display": "none"},
                        ),
                    },
                    {
                        "key": "修改密码",
                        "label": "修改密码",
                        "children": fac.AntdCard(
                            fac.AntdCardMeta(
                                description=fac.AntdForm(
                                    fac.AntdFormItem(
                                        fac.AntdSpace(
                                            [
                                                fac.AntdInput(
                                                    placeholder="请输入旧密码",
                                                    mode="password",
                                                    id='old-password',
                                                    passwordUseMd5=True
                                                ),
                                                fac.AntdInput(
                                                    placeholder="请输入新密码",
                                                    mode="password",
                                                    id='new-password',
                                                    passwordUseMd5=True
                                                ),
                                                fac.AntdInput(
                                                    placeholder="请再次输入新密码",
                                                    mode="password",
                                                    id='confirm-new-password',
                                                    passwordUseMd5=True
                                                ),
                                                fac.AntdButton("确认修改", type="primary", id='submit-new-password'),
                                            ],
                                            direction="vertical",
                                        ),
                                        label="密码修改",
                                    ),
                                    style={
                                        'width': '100%',
                                        'height': '100%'
                                    }
                                )
                            ),
                            title="安全设置",
                            hoverable=True,
                            bodyStyle={
                                'display': 'flex',
                                'alignItems': 'center',
                                'justifyContent': 'center'
                            },
                            style={
                                'width': '75%',
                                'height': '100%'
                            }
                        ),
                    },
                ],
                tabPosition='left',
                type='card',
                tabPaneAnimated=True,
                style={
                    'width': '50%',
                    'height': '60%',
                    'paddingTop': '10px',
                    'paddingBottom': '10px'
                },
            ),
            html.Div(id='user-page-message-container')
        ],
        style={"height": "100%"},
    )

    return content




