import dash
from dash import Input, Output, State
from server import app


@app.callback(
    Output('select-table', 'columns'),
    Input('sortable-list', 'currentOrder')
)
def sortable_columns(currentOrder):
    if currentOrder:
        
        return [
            {
                'dataIndex': str(i),
                'title': str(i)
            } for i in currentOrder
        ]
    return []


@app.callback(
    [
        Output('sortable-list', 'items'),
        Output('sortable-list', 'currentOrder')
    ],
    [
        Input('columns-selected', 'moveDirection'),
        Input('columns-selected', 'targetKeys')
    ],
    [
        State('columns-selected', 'moveKeys'),
        State('sortable-list', 'currentOrder')
    ]
)
def select_columns(moveDirection, targetKeys, moveKeys, old_currentOrder: list):
    if not targetKeys:
        return [[], []]
    if moveDirection:
        items = [
            {
                'key': str(i),
                'content': str(i),
                'style': {
                    'width': '100px'
                }
            } for i in targetKeys
        ] if targetKeys else []
        new_currendOrder = (
            old_currentOrder + [*moveKeys]
            if moveDirection == 'right' else [new for new in old_currentOrder if new not in moveKeys]
        )
        return [items, new_currendOrder]
    return dash.no_update   