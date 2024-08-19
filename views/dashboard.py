import random
import pandas as pd
import feffery_antd_charts as fact
import feffery_antd_components as fac
import feffery_utils_components as fuc

from dash import html


def render_dashboard_content():
    
    content = [
        fac.AntdRow(
            [
                fac.AntdCol(
                    fac.AntdCard(
                        fac.AntdFlex(
                            [
                                html.Div(
                                    fac.AntdStatistic(
                                        value=fuc.FefferyCountUp(
                                            end=235406,
                                            duration=3,
                                            enableScrollSpy=True
                                        ),
                                        prefix='¥',
                                        suffix='元',
                                        title='销售额'
                                    )
                                ),
                                html.Div(
                                    fac.AntdProgress(
                                        percent=80,
                                        strokeColor={'from': '#08D4B2', 'to': '#00FBD1'}
                                    ),
                                    style={
                                        'height': '50%'
                                    }
                                ),
                                fac.AntdDivider(style={'margin': '12px 0'}),
                                fac.AntdFlex(
                                    [
                                        fac.AntdText(
                                            [
                                                '周同比',
                                                fac.AntdIcon(
                                                    icon='antd-rise',
                                                    style={'color': '#f5222d'}
                                                ),
                                                '12%'
                                            ]
                                        ),
                                        fac.AntdText(
                                            [
                                                '日同比',
                                                fac.AntdIcon(
                                                    icon='antd-fall',
                                                    style={'color': '#52c41a'}
                                                ),
                                                '10%'
                                            ]
                                        ),
                                    ],
                                    gap=10
                                )
                            ],
                            vertical=True,
                            style={
                                'width': '100%'
                            }
                        ),
                        style={
                            'width': '100%'
                        },
                        headStyle={
                            'display': 'none'
                        },
                        hoverable=True
                    ),
                    xs=15,
                    sm=15,
                    md=10,
                    lg=5,
                    xl=5,
                    xxl=5
                ),
                fac.AntdCol(
                    fac.AntdCard(
                        fac.AntdFlex(
                            [
                                html.Div(
                                    fac.AntdStatistic(
                                        value=fuc.FefferyCountUp(
                                            end=456,
                                            duration=3,
                                            enableScrollSpy=True
                                        ),
                                        suffix='件',
                                        title='销量'
                                    )
                                ),
                                html.Div(
                                    fact.AntdTinyLine(
                                        data=[random.randint(300, 500) for i in range(1, 16)],
                                        smooth=True,
                                        autoFit=True
                                    ),
                                    style={
                                        'height': '50%'
                                    }
                                ),
                                fac.AntdDivider(style={'margin': '12px 0'}),
                                fac.AntdFlex(
                                    [
                                        fac.AntdText(
                                            [
                                                '周同比',
                                                fac.AntdIcon(
                                                    icon='antd-fall',
                                                    style={'color': '#52c41a'}
                                                ),
                                                '12%'
                                            ]
                                        ),
                                        fac.AntdText(
                                            [
                                                '日同比',
                                                fac.AntdIcon(
                                                    icon='antd-rise',
                                                    style={'color': '#f5222d'}
                                                ),
                                                '10%'
                                            ]
                                        ),
                                    ],
                                    gap=10
                                )
                            ],
                            vertical=True,
                            style={
                                'width': '100%'
                            }
                        ),
                        style={
                            'width': '100%'
                        },
                        headStyle={
                            'display': 'none'
                        },
                        hoverable=True
                    ),
                    xs=15,
                    sm=15,
                    md=10,
                    lg=5,
                    xl=5,
                    xxl=5
                ),
                fac.AntdCol(
                    fac.AntdCard(
                        fac.AntdFlex(
                            [
                                html.Div(
                                    fac.AntdStatistic(
                                        value=fuc.FefferyCountUp(
                                            end=6586,
                                            duration=3,
                                            enableScrollSpy=True
                                        ),
                                        suffix='笔',
                                        title='支付笔数'
                                    )
                                ),
                                html.Div(
                                    fact.AntdTinyColumn(
                                        data=[random.randint(3000, 7000) for i in range(15)],
                                        autoFit=True
                                    ),
                                    style={
                                        'height': '50%'
                                    }
                                ),
                                fac.AntdDivider(style={'margin': '12px 0'}),
                                fac.AntdFlex(
                                    [
                                        fac.AntdText(
                                            [
                                                '转化率: 60%'
                                            ]
                                        ),
                                        fac.AntdText(
                                            [
                                                '同比',
                                                fac.AntdIcon(
                                                    icon='antd-fall',
                                                    style={'color': '#52c41a'}
                                                ),
                                                '10%'
                                            ]
                                        ),
                                    ],
                                    gap=10
                                )
                            ],
                            vertical=True,
                            style={
                                'width': '100%'
                            }
                        ),
                        style={
                            'width': '100%'
                        },
                        headStyle={
                            'display': 'none'
                        },
                        hoverable=True
                    ),
                    xs=15,
                    sm=15,
                    md=10,
                    lg=5,
                    xl=5,
                    xxl=5
                ),
                fac.AntdCol(
                    fac.AntdCard(
                        fac.AntdFlex(
                            [
                                html.Div(
                                    fac.AntdStatistic(
                                        value=fuc.FefferyCountUp(
                                            end=36879,
                                            duration=3,
                                            enableScrollSpy=True
                                        ),
                                        suffix='次',
                                        title='访问量'
                                    )
                                ),
                                html.Div(
                                    fact.AntdTinyLine(
                                        data=[random.randint(5000, 40000) for i in range(15)],
                                        lineStyle={
                                            'stroke': '#00D084'
                                        },
                                        smooth=True,
                                        autoFit=True
                                    ),
                                    style={
                                        'height': '50%'
                                    }
                                ),
                                fac.AntdDivider(style={'margin': '12px 0'}),
                                fac.AntdFlex(
                                    [
                                        fac.AntdText(
                                            [
                                                '周同比',
                                                fac.AntdIcon(
                                                    icon='antd-rise',
                                                    style={'color': '#f5222d'}
                                                ),
                                                '12%'
                                            ]
                                        ),
                                        fac.AntdText(
                                            [
                                                '日同比',
                                                fac.AntdIcon(
                                                    icon='antd-fall',
                                                    style={'color': '#52c41a'}
                                                ),
                                                '10%'
                                            ]
                                        ),
                                    ],
                                    gap=10
                                )
                            ],
                            vertical=True,
                            style={
                                'width': '100%'
                            }
                        ),
                        style={
                            'width': '100%'
                        },
                        headStyle={
                            'display': 'none'
                        },
                        hoverable=True
                    ),
                    xs=15,
                    sm=15,
                    md=10,
                    lg=5,
                    xl=5,
                    xxl=5
                ),
            ],
            style={
                'width': '100%'
            },
            justify='space-around',
            gutter=[15, 15]
        )
    ]

    return content