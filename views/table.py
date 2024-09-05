import feffery_antd_components as fac
import feffery_utils_components as fuc
import numpy as np
import pandas as pd
from dash import html

from callbacks import table_c

df = pd.DataFrame(
    {
        f'字段tttttttttttttttttttttttttttt{i}': [np.random.randint(5000, 10000) for v in range(10)]
        for i in range(30)
    }
)


def render_table_content(columns_data: dict, table=df):

    _columns = [
        {
            'dataIndex': i,
            'title': i,
            'width': '200px',
            'fixed': 'left' if i in columns_data['pinned_columns'] else None
        } for i in columns_data['column_sorted']
    ] if columns_data['column_sorted'] else [
        {
            'dataIndex': i,
            'title': i,
            'width': '200px',
            'fixed': 'left' if i in columns_data['pinned_columns'] else None
        } for i in table.columns
    ]

    content = fac.AntdCenter(
        fac.AntdCard(
            [
                fac.AntdRow(
                    fac.AntdCol(
                        [
                            fac.AntdTabs(
                                items=[
                                    {
                                        'key': '查询表格',
                                        'label': '查询表格',
                                        'children': fac.AntdRow(
                                            fac.AntdCol(
                                                fac.AntdTable(
                                                    id='select-table',
                                                    data=table.to_dict('records'),
                                                    columns=_columns,
                                                    maxWidth=900
                                                ),
                                                span=24,
                                                style={
                                                    'maxWidth': '100%'
                                                }
                                            ),
                                            style={
                                                'width': '100%'
                                            },
                                            justify='center'
                                        )
                                    }
                                ],
                                tabBarRightExtraContent=fac.AntdFlex(
                                    [
                                        fac.AntdPopconfirm(
                                            fac.AntdIcon(
                                                icon='antd-pushpin',
                                            ),
                                            description=fac.AntdTransfer(
                                                id='select-columns-pinned',
                                                dataSource=[
                                                    {
                                                        'key': i,
                                                        'title': i,
                                                    } for i in table.columns
                                                ],
                                                targetKeys=columns_data['pinned_columns'], # 避免出现类型错误
                                                showSearch=True
                                            ),
                                            title='固定列',
                                            placement='left',
                                            okText='保存并应用',
                                            icon='',
                                            id='pinned-popconfirm'
                                        ),
                                        fac.AntdPopconfirm(
                                            fac.AntdIcon(
                                                icon='antd-setting'
                                            ),
                                            description=fac.AntdFlex(
                                                [
                                                    fac.AntdTransfer(
                                                        id='columns-selected',
                                                        dataSource=[
                                                            {
                                                                'key': i,
                                                                'title': i,
                                                            } for i in table.columns
                                                        ],
                                                        targetKeys=columns_data['column_sorted'],
                                                        showSearch=True
                                                    ),
                                                    fac.AntdFlex(
                                                        [
                                                            fac.AntdText('拖拽排序'),
                                                            fuc.FefferySortable(
                                                                id='sortable-list',
                                                                items=[
                                                                    {
                                                                        'key': str(i),
                                                                        'content': str(i),
                                                                        'style': {
                                                                            'width': '100px'
                                                                        }
                                                                    } for i in table.columns
                                                                ],
                                                                style={
                                                                    'maxHeight': '200px',
                                                                    'maxWidth': '200px',
                                                                    'width': '175px',
                                                                    'overflowX': 'scroll',
                                                                    'overflowY': 'scroll'
                                                                },
                                                                handlePosition='start',
                                                                currentOrder=columns_data['column_sorted']
                                                            ),
                                                        ],
                                                        vertical=True,
                                                        gap=5
                                                    )
                                                ],
                                                gap=20
                                            ),
                                            placement='left',
                                            title='列排序',
                                            icon='',
                                            okText='保存应用',
                                            id='columns-editor-confirm'
                                        )
                                    ],
                                    gap=15
                                ),
                            )
                        ],
                        span=24
                    ),
                    style={
                        'width': '100%'
                    }
                ),
                html.Div(
                    id='save-columns-data-message'
                )
            ],
            style={
                'width': '100%'
            },
            headStyle={'display': 'none'}
        ),
        style={
            'width': '100%'
        }
    )

    return content