import calendar
import datetime
from itertools import product

import dash
import feffery_antd_charts as fact
import feffery_antd_components as fac
import numpy as np
import pandas as pd
from dash import set_props
from dash.dependencies import Input, Output, State
from flask_jwt_extended import jwt_required
from flask_login import current_user

from models.model import is_authorized
from server import app

demo_data = pd.DataFrame(
    product(
        ["华北地区", "华南地区", "华东地区", "西南地区", "西北地区", "东北地区"],
        [f"{i}月" for i in range(1, 7)],
        [f"品类{i}" for i in "ABCDE"],
    ),
    columns=["业务地区", "月份", "品类"],
)
demo_data["销售额(万)"] = np.round(np.random.uniform(10, 500, demo_data.shape[0]), 2)


@app.callback(
    Output('date-range-picker', 'value'),
    Input('date-range-segmented', 'value')
)
@is_authorized(user=current_user, view='概览')
@jwt_required()
def date_range_function(value):
    if value:
        today_date = datetime.datetime.today().date()
        if value == '本日':
            return [str(today_date), str(today_date)]
        elif value == '本周':
            return [
                str(today_date - datetime.timedelta(days=today_date.weekday())),
                str(
                    (today_date - datetime.timedelta(days=today_date.weekday())) + datetime.timedelta(days=6)
                )
            ]
        elif value == '本月':
            return [
                str(datetime.datetime(today_date.year, today_date.month, 1)),
                str(
                    datetime.datetime(
                        today_date.year, 
                        today_date.month,
                        calendar.monthrange(today_date.year, today_date.month)[1]
                    )
                )
            ]
        else:
            return [
                str(datetime.datetime(today_date.year, 1, 1)),
                str(datetime.datetime(today_date.year, 12, 31))
            ]
        

@app.callback(
    [
        Output("drill-level-indicator-container", "children"),
        Output("drill-level-tip", "children"),
        Output("drill-chart-container", "children"),
    ],
    Input("drill-level-state", "data"),
)
@is_authorized(user=current_user, view='概览')
@jwt_required()
def update_drill_views(data):
    # 根据当前level参数，构造图表数据
    if data["current"] == "根节点":
        return [
            fac.AntdBreadcrumb(id="drill-level-indicator", items=[{"title": "根节点"}]),
            fac.AntdText(data["level_tips"]["根节点"], type="secondary"),
            fact.AntdPie(
                id={"type": "drill-chart", "level": "根节点"},
                data=demo_data.groupby("业务地区", as_index=False)
                .agg({"销售额(万)": "sum"})
                .to_dict("records"),
                angleField="销售额(万)",
                colorField="业务地区",
                innerRadius=0.8,
                radius=0.9,
                label={
                    "formatter": {
                        "func": """(e) => `${e['业务地区']}\n${e['销售额(万)'].toFixed(2)}万`"""
                    }
                },
                statistic={
                    "title": {"content": "总销售额"},
                    "content": {
                        "content": "{}万".format(demo_data["销售额(万)"].sum().round(2))
                    },
                },
                legend=False,
                tooltip=False,
            ),
        ]

    elif data["current"] == "业务地区":
        return [
            fac.AntdBreadcrumb(
                id="drill-level-indicator",
                items=[
                    {"title": "根节点"},
                    *[
                        {"title": condition}
                        for condition in data["current_level_conditions"]
                    ],
                ],
            ),
            fac.AntdText(data["level_tips"]["业务地区"], type="secondary"),
            fact.AntdColumn(
                id={"type": "drill-chart", "level": "业务地区"},
                data=demo_data.query(
                    '业务地区 == "{}"'.format(data["current_level_conditions"][-1])
                )
                .groupby("月份", as_index=False)
                .agg({"销售额(万)": "sum"})
                .to_dict("records"),
                xField="月份",
                yField="销售额(万)",
                label={
                    "formatter": {
                        "func": """(e) => `${e['销售额(万)'].toFixed(2)}万`"""
                    }
                },
                legend=False,
                tooltip=False,
            ),
        ]

    elif data["current"] == "月份":
        return [
            fac.AntdBreadcrumb(
                id="drill-level-indicator",
                items=[
                    {"title": "根节点"},
                    *[
                        {"title": condition}
                        for condition in data["current_level_conditions"]
                    ],
                ],
            ),
            fac.AntdText(data["level_tips"]["月份"], type="secondary"),
            fact.AntdBar(
                id={"type": "drill-chart", "level": "月份"},
                data=demo_data.query(
                    '业务地区 == "{}" and 月份 == "{}"'.format(
                        data["current_level_conditions"][-2],
                        data["current_level_conditions"][-1],
                    )
                )
                .groupby("品类", as_index=False)
                .agg({"销售额(万)": "sum"})
                .sort_values("销售额(万)", ascending=False)
                .to_dict("records"),
                xField="销售额(万)",
                yField="品类",
                label={
                    "formatter": {
                        "func": """(e) => `${e['销售额(万)'].toFixed(2)}万`"""
                    }
                },
                legend=False,
                tooltip=False,
            ),
        ]


@app.callback(
    Input({"type": "drill-chart", "level": "根节点"}, "recentlySectorClickRecord"),
    State("drill-level-state", "data"),
)
@is_authorized(user=current_user, view='概览')
@jwt_required()
def handle_root_level_event(recentlySectorClickRecord, data):
    if recentlySectorClickRecord["data"]:
        set_props(
            "drill-level-state",
            {
                "data": {
                    **data,
                    "current": "业务地区",
                    "current_level_conditions": [
                        recentlySectorClickRecord["data"]["业务地区"]
                    ],
                }
            },
        )



@app.callback(
    Input({"type": "drill-chart", "level": "业务地区"}, "recentlyColumnClickRecord"),
    State("drill-level-state", "data"),
)
@is_authorized(user=current_user, view='概览')
@jwt_required()
def handle_area_level_event(recentlyColumnClickRecord, data):
    if recentlyColumnClickRecord["data"]:
        set_props(
            "drill-level-state",
            {
                "data": {
                    **data,
                    "current": "月份",
                    "current_level_conditions": [
                        *data["current_level_conditions"],
                        recentlyColumnClickRecord["data"]["月份"],
                    ],
                }
            },
        )



@app.callback(
    Input("drill-level-indicator", "clickedItem"),
    [State("drill-level-state", "data"), State("drill-level-indicator", "items")],
)
@is_authorized(user=current_user, view='概览')
@jwt_required()
def handle_indicator_click_switch_level(clickedItem, data, items):
    # 计算当前点击层级下标
    items = [item["title"] for item in items]
    clickedItem = clickedItem["itemTitle"]
    clicked_level_index = items.index(clickedItem)

    # 避免多余的回调数据返回
    if data["current"] != data["levels"][clicked_level_index]:
        # 根据clicked_level_index更新层级状态
        set_props(
            "drill-level-state",
            {
                "data": {
                    **data,
                    "current": data["levels"][clicked_level_index],
                    "current_level_conditions": data["current_level_conditions"][
                        :clicked_level_index
                    ],
                }
            },
        )