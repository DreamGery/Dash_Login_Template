import random
import feffery_antd_charts as fact
import feffery_antd_components as fac
import feffery_utils_components as fuc
import pandas as pd

from dash import html
from feffery_antd_components.utils import df2table

def render_dashboard_content():
    
    data = pd.DataFrame(
        {
            'date': pd.date_range('2024-07-1', '2024-07-15'),
            'value': [random.randint(4000, 6000) for i in range(15)]
        }
    )

    table_data = pd.DataFrame(
        {
            '店铺名称': [f'店铺{i}' for i in range(5)],
            '销售额': [random.randint(800, 1200) for i in range(5)]
        }
    )

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
                                        'height': '80%'
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
                        bodyStyle={
                            'padding': '20px 24px 8px'
                        },
                        hoverable=True
                    ),
                    xs=15,
                    sm=15,
                    md=10,
                    lg=6,
                    xl=6,
                    xxl=6
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
                                        'height': '80%'
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
                        bodyStyle={
                            'padding': '20px 24px 8px'
                        },
                        hoverable=True
                    ),
                    xs=15,
                    sm=15,
                    md=10,
                    lg=6,
                    xl=6,
                    xxl=6
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
                                        'height': '80%'
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
                        bodyStyle={
                            'padding': '20px 24px 8px'
                        },
                        hoverable=True
                    ),
                    xs=15,
                    sm=15,
                    md=10,
                    lg=6,
                    xl=6,
                    xxl=6
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
                                        'height': '80%'
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
                        bodyStyle={
                            'padding': '20px 24px 8px'
                        },
                        hoverable=True
                    ),
                    xs=15,
                    sm=15,
                    md=10,
                    lg=6,
                    xl=6,
                    xxl=6
                ),
            ],
            style={
                'width': '100%',
                'marginBottom': '50px'
            },
            justify='space-between',
            gutter=[15, 15]
        ),
        fac.AntdRow(
            [
                fac.AntdCol(
                    [
                        fac.AntdCard(
                            fac.AntdTabs(
                                items=[
                                    {
                                        'key': i,
                                        'label': i,
                                        'children': [
                                            fac.AntdRow(
                                                [
                                                    fac.AntdCol(
                                                        fact.AntdArea(
                                                            data=data.to_dict('records'),
                                                            smooth=True,
                                                            yField='value',
                                                            xField='date',
                                                            autoFit=True
                                                        ),
                                                        xs=24,
                                                        sm=24,
                                                        md=24,
                                                        lg=15,
                                                        xl=15,
                                                        xxl=15,
                                                        style={
                                                            'height': '400px'
                                                        }
                                                    ),
                                                    fac.AntdCol(
                                                        fac.AntdFlex(
                                                            [
                                                                fac.AntdText(
                                                                    '各店铺销售额',
                                                                    style={
                                                                        'fontWeight': 700,
                                                                        'fontSize': '18px'
                                                                    }
                                                                ),
                                                                df2table(
                                                                    raw_df=table_data,
                                                                    pagination=False
                                                                ),
                                                            ],
                                                            vertical=True,
                                                            gap=18
                                                        ),
                                                        xs=24,
                                                        sm=24,
                                                        md=24,
                                                        lg=8,
                                                        xl=8,
                                                        xxl=8,
                                                        style={
                                                            'height': '400px'
                                                        }
                                                    )
                                                ],
                                                justify='space-between',
                                                align='middle'
                                            )
                                        ]
                                    } for i in ['销量', '销售额']
                                ],
                                style={
                                    'width': '100%'
                                },
                                size='large',
                                tabBarRightExtraContent=fac.AntdDateRangePicker(value=['2024-07-01', '2024-07-15']),
                                tabPaneAnimated=True
                            ),
                            headStyle={'display': 'none'},
                            bodyStyle={
                                'paddingTop': '12px' 
                            },
                            style={
                                'width': '100%'
                            }
                        )
                    ],
                    span=24
                )
            ],
            style={
                'width': '100%'
            },
            gutter=[15, 15],
            justify='space-between'
        )
    ]

    return content