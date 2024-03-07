from dash import Dash, html, Input, Output, State, dcc
import time
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Button("开始计算", id="button-calculate", n_clicks=0, className="me-2"),
    dcc.Loading(id="loading", children=[html.Div(id="calculation-status")]),
])

@app.callback(
    [Output("calculation-status", "children", allow_duplicate=True),
     Output("button-calculate", "disabled", allow_duplicate=True)],
    [Input("button-calculate", "n_clicks")],
    [State("calculation-status", "children")],
    prevent_initial_call=True
)
def trigger_calculation(n_clicks, status):
    # 判断是否是按钮触发的回调
    if n_clicks > 0:
        return "计算中...", True
    return dash.no_update

@app.callback(
    [Output("calculation-status", "children"),
     Output("button-calculate", "disabled")],
    [Input("calculation-status", "children")],
    prevent_initial_call=True
)
def perform_calculation(status):
    # 判断是否是状态更新触发的回调
    if status == "计算中...":
        # 模拟耗时计算
        time.sleep(5)
        return "计算完成", False
    return dash.no_update

if __name__ == "__main__":
    app.run_server(debug=True)
