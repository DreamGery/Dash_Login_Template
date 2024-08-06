import dash
import feffery_antd_components as fac

from dash import html

app = dash.Dash(__name__)

app.layout = html.Div(
    fac.AntdTabs(
        items=[
            {
                "key": "基本信息",
                "label": "基本信息",
                "children": fac.AntdCard(
                    [
                        fac.AntdCardMeta(
                            avatar=fac.AntdAvatar(size="large"),
                            title="用户信息",
                            description=[
                                fac.AntdForm(
                                    [
                                        fac.AntdFormItem(
                                            fac.AntdUpload(
                                                buttonContent="点击更改头像",
                                                fileTypes=["jpg", "jpeg", "png"],
                                            ),
                                        ),
                                        fac.AntdFormItem(
                                            fac.AntdSpace(
                                                [
                                                    fac.AntdInput(value="DreamGery"),
                                                    fac.AntdButton(
                                                        "确认修改", type="primary"
                                                    ),
                                                ]
                                            ),
                                            label="昵称",
                                        ),
                                        fac.AntdFormItem(
                                            fac.AntdSelect(
                                                options=[],
                                                value=[f"权限{i}" for i in range(5)],
                                                readOnly=True,
                                                mode="multiple",
                                                disabled=True,
                                            ),
                                            label="权限",
                                        ),
                                    ],
                                    layout="vertical",
                                    style={"height": "500px"},
                                )
                            ],
                        )
                    ],
                    style={"width": "500px"},
                    bordered=False,
                    hoverable=True,
                    headStyle={"display": "none"},
                ),
            },
            {
                "key": "修改密码",
                "label": "修改密码",
                "children": fac.AntdCard(
                    fac.AntdCardMeta(
                        description=fac.AntdForm(
                            fac.AntdFormItem(
                                fac.AntdSpace(
                                    [
                                        fac.AntdInput(
                                            placeholder="请输入旧密码",
                                            mode="password",
                                        ),
                                        fac.AntdInput(
                                            placeholder="请输入新密码",
                                            mode="password",
                                        ),
                                        fac.AntdInput(
                                            placeholder="请再次输入新密码",
                                            mode="password",
                                        ),
                                        fac.AntdButton("确认修改", type="primary"),
                                    ],
                                    direction="vertical",
                                ),
                                label="密码修改",
                            ),
                        )
                    ),
                    title="安全设置",
                    hoverable=True,
                    style={
                        'width': '25%'
                    }
                ),
            },
        ],
        tabPosition="left",
        type="card",
        style={"height": "100%"},
        tabPaneAnimated=True,
    ),
    style={"height": "100vh"},
)


if __name__ == "__main__":
    app.run(debug=True)
