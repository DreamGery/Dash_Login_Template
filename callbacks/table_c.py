import dash
import feffery_antd_components as fac
from dash import Input, Output, State, set_props
from flask_jwt_extended import jwt_required
from flask_login import current_user

from models.model import auth, is_authorized
from server import app


@app.callback(
    [
        Output('select-table', 'columns', allow_duplicate=True)
    ],
    [
        Input('columns-editor-confirm', 'confirmCounts'),
        Input('pinned-popconfirm', 'confirmCounts'),
    ],
    [
        State('select-columns-pinned', 'targetKeys'),
        State('sortable-list', 'currentOrder')
    ],
    prevent_initial_call=True
)
@is_authorized(user=current_user, view='查询表格')
@jwt_required()
def sortable_columns(confirmCounts_editor, pinned_confirmCounts, targetKeys, currentOrder):
    if confirmCounts_editor or pinned_confirmCounts:
        update_message = auth.change_user_information(
            username=current_user.username,
            changed_data={
                'select_table_columns': {
                    'column_sorted': currentOrder,
                    'pinned_columns': targetKeys
                }
            }
        )
        if update_message['status'] == 'success':
            set_props(
                'save-columns-data-message',
                {
                    'children': fac.AntdMessage(
                        type='success',
                        content='保存成功'
                    )
                }
            )
        else:
            set_props(
                'save-columns-data-message',
                {
                    'children': fac.AntdMessage(
                        type='error',
                        content='保存失败'
                    )
                }
            )

    if currentOrder:
        columns = [
            {
                'dataIndex': str(i),
                'title': str(i),
                'fixed': 'left' if i in targetKeys else None,
                'width': '200px'
            } for i in currentOrder
        ]
        return [columns]
    
    return [[]]




@app.callback(
    [
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
@is_authorized(user=current_user, view='查询表格')
@jwt_required()
def select_columns(moveDirection, targetKeys, moveKeys, old_currentOrder: list):
    if not targetKeys:
        return [[]]
    if moveDirection:
        new_currendOrder = (
            old_currentOrder + [*moveKeys]
            if moveDirection == 'right' else [new for new in old_currentOrder if new not in moveKeys]
        )
        return [new_currendOrder]
    return dash.no_update


