import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component

from callbacks import login_c  # noqa: F401


def render_login_content() -> Component:
    content = html.Div(
        [
            fac.AntdRow(
                [
                    fac.AntdCol(
                        fac.AntdSpace(
                            [
                                fac.AntdSpace(
                                    [
                                        html.Img(
                                            src='https://fac.feffery.tech/assets/imgs/fac-logo.svg',
                                            style={
                                                'width': '44px',
                                                'height': '44px'
                                            }
                                        ),
                                        fac.AntdText(
                                            'Ant Design',
                                            style={
                                                'fontWeight': '600',
                                                'fontSize': '33px'
                                            }
                                        ),
                                    ]
                                ),
                                fac.AntdTabs(
                                    id='tabs',
                                    items=[
                                        {
                                            'label': '账号密码登录',
                                            'key': '账号密码登录',
                                            'children': fac.AntdCenter(
                                                fac.AntdForm(
                                                    [
                                                        fac.AntdFormItem(
                                                            fac.AntdInput(
                                                                prefix=fac.AntdIcon(icon='antd-user'),
                                                                placeholder='用户名',
                                                                size='large',
                                                                id='username-input'
                                                            ),
                                                            id='form-item-username'
                                                        ),
                                                        fac.AntdFormItem(
                                                            fac.AntdInput(
                                                                prefix=fac.AntdIcon(icon='antd-lock'),
                                                                mode='password',
                                                                placeholder='密码',
                                                                size='large',
                                                                passwordUseMd5=True,
                                                                id='password-input'
                                                            ),
                                                            id='form-item-password'
                                                        ),
                                                        fac.AntdFormItem(
                                                            fac.AntdCheckbox(
                                                                label='记住密码',
                                                                id='remember',
                                                                checked=False # 确保初始回调时, checked值为bool类型
                                                            )
                                                        ),
                                                        fac.AntdFormItem(
                                                            fac.AntdButton(
                                                                '登录', 
                                                                type='primary', 
                                                                block=True,
                                                                size='large',
                                                                id='login-submit'
                                                            )
                                                        ),
                                                    ],
                                                    style={
                                                        'width': '300px',
                                                        'padding': '5px 5px 5px 5px'
                                                    }
                                                )
                                            )
                                        }
                                    ],
                                    centered=True,
                                    style={
                                        'display': 'none'
                                    }
                                )
                            ],
                            style={
                                'width': '100%'
                            },
                            direction='vertical',
                            align='center',
                            size=25
                        ),
                        id='login-content-container',
                        span=20
                    )
                ],
                justify='center',
                style={
                    'transform': 'translateY(50px)'
                }
            )
        ],
        style={
            'width': '100vw',
            'height': '100vh',
            'backgroundImage': 'url("https://mdn.alipayobjects.com/yuyan_qk0oxh/afts/img/V-_oS6r-i7wAAAAAAAAAAAAAFl94AQBr")',
            'backgroundSize': '100% 100%'
        }
    )

    return content