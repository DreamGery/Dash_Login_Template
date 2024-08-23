import calendar
import datetime
import dash

from dash.dependencies import Input, Output
from server import app




@app.callback(
    Output('date-range-picker', 'value'),
    Input('date-range-segmented', 'value')
)
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
        