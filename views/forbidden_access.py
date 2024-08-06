import feffery_antd_components as fac
from dash import html
from dash.dependencies import Component


def render_access_content() -> Component:

    return html.Div(
        [
            html.Div(
                [
                    fac.AntdResult(
                        status='403',
                        title='无权访问',
                        subTitle='请联系管理员开通权限',
                        style={
                            'paddingBottom': 0,
                            'paddingTop': 0
                        }
                    ),
                ],
                style={
                    'textAlign': 'center'
                }
            )
        ],
        style={
            'height': '100%',
            'display': 'flex',
            'alignItems': 'center',
            'justifyContent': 'center'
        }
    )