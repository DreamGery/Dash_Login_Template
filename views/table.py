import feffery_antd_components as fac
import feffery_utils_components as fuc
import pandas as pd
import numpy as np

from callbacks import table_c

df = pd.DataFrame(
    {
        f'字段{i}': [np.random.randint(5000, 10000) for v in range(10)]
        for i in range(5)
    }
)


def render_table_content(table=df):

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
                                        'children': fac.AntdTable(
                                            id='select-table',
                                            data=table.to_dict('records'),
                                            columns=[
                                                {
                                                    'title': i,
                                                    'dataIndex': i
                                                } for i in table.columns
                                            ]
                                        )
                                    }
                                ],
                                tabBarRightExtraContent=fac.AntdPopover(
                                    fac.AntdIcon(
                                        icon='antd-setting'
                                    ),
                                    content=fac.AntdFlex(
                                        [
                                            fac.AntdTransfer(
                                                id='columns-selected',
                                                dataSource=[
                                                    {
                                                        'key': i,
                                                        'title': i
                                                    } for i in table.columns
                                                ],
                                                targetKeys=[i for i in table.columns]
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
                                                                    'width': '75px'
                                                                }
                                                            } for i in table.columns
                                                        ]
                                                    )
                                                ],
                                                vertical=True,
                                                gap=5
                                            )
                                        ],
                                        gap=20,
                                        style={
                                            'paddingRight': '5px'
                                        }
                                    )
                                )
                            )
                        ],
                        span=24
                    ),
                    style={
                        'width': '100%'
                    }
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