import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash import dcc, html
from dash.dependencies import Component

from callbacks import index_c  # noqa: F401
from config import MenuConfig


def render_index_content(username, permission) -> Component:
    content = html.Div(
        [
            fac.AntdConfigProvider(
                fac.AntdLayout(
                    [
                        fac.AntdAffix(
                            fac.AntdHeader(
                                fac.AntdRow(
                                    [
                                        fac.AntdCol(
                                            fac.AntdFlex(
                                                [
                                                    html.Img(
                                                        src='https://fac.feffery.tech/assets/imgs/fac-logo.svg',
                                                        style={
                                                            'height': '32px',
                                                            'width': '32px'
                                                        }
                                                    ),
                                                    fac.AntdText(
                                                        'Ant Design',
                                                        style={
                                                            'fontSize': '18px',
                                                            'fontWeight': '700',
                                                        },
                                                        className='header-title'
                                                    )
                                                ],
                                                align='center',
                                                gap='middle'
                                            ),
                                            span=10,
                                            style={
                                                'display': 'flex',
                                                'alignItems': 'center'
                                            }
                                        ),
                                        fac.AntdCol(
                                            fac.AntdFlex(
                                                [   
                                                    fac.AntdSwitch(
                                                        id='mode',
                                                        unCheckedChildren=html.Img(
                                                            src='./assets/img/sun.svg',
                                                            style={
                                                                'width': '20px',
                                                                'height': '100%'
                                                            }
                                                        ),
                                                        checkedChildren=html.Img(
                                                            src='./assets/img/weather-color_moon-stars.svg',
                                                            style={
                                                                'width': '20px',
                                                                'height': '100%'
                                                            }
                                                        ),
                                                        className={
                                                            '.ant-switch-inner .ant-switch-inner-unchecked': {
                                                                'marginTop': '-25px'
                                                            }
                                                        },
                                                        persistence=True
                                                    ),
                                                    fac.AntdDropdown(
                                                        [
                                                            fac.AntdFlex(
                                                                [
                                                                    fac.AntdAvatar(
                                                                        mode='text',
                                                                        text=username[0],
                                                                    ),
                                                                    fac.AntdText(
                                                                        username,
                                                                        className='username-text'
                                                                    )
                                                                ],
                                                                align='center',
                                                                gap='small'
                                                            )
                                                        ],
                                                        menuItems=[
                                                            {
                                                                'title': '退出登录',
                                                                'icon': 'antd-logout',
                                                                'key': 'logout'
                                                            }
                                                        ],
                                                        id='header-dropdown-menu'
                                                    ),
                                                ],
                                                align='center',
                                                gap=20
                                            ),
                                            span=6,
                                            style={
                                                'display': 'flex',
                                                'alignItems': 'center',
                                                'justifyContent': 'right'
                                            }
                                        )
                                    ],
                                    style={
                                        'width': '100%',
                                        'height': '100%'
                                    },
                                    justify='space-between'
                                ),
                                id='header',
                                style={
                                    "backgroundColor": "rgba(255, 255, 255, 1)",
                                    'backdropFilter': 'blur(10px)',
                                    'borderBlockEnd': '1px solid rgba(5, 5, 5, 0.06)',
                                    'transition': 'background-color 1s ease'
                                },
                            ),
                            offsetBottom=64
                        ),
                        fac.AntdLayout(
                            [
                                fac.AntdSider(
                                    fac.AntdMenu(
                                        defaultSelectedKey="图标antd-home",
                                        menuItems=MenuConfig().return_menu_items(permission=permission),
                                        mode="inline",
                                        style={
                                            'overflow': 'auto',
                                            'maxHeight': '80%'
                                        },
                                        id='menu'
                                    ),
                                    collapsible=True,
                                    theme="light",
                                    breakpoint='lg',
                                    id='antd-sider'
                                ),
                                fac.AntdLayout(
                                    [
                                        fac.AntdContent(
                                            id='content-container',
                                            style={
                                                'padding': '10px 10px 0px 10px',
                                            }
                                        )
                                    ]
                                ),
                            ],
                        ),
                    ],
                    style={
                        'minHeight': '100%'
                    }
                ),
                id='config'
            ),
            fuc.FefferyListenScroll(id='scroll-listener'),
            fuc.FefferyResponsive(
                id='breakpoint-listener'
            ),
            # 注入轮询组件 用来更新JWT 45分钟触发一次
            dcc.Interval(
                id='jwt-interval',
                interval=1000 * 60 * 45
            )
        ],
        style={
            "height": '100vh'
        }
    )

    return content

