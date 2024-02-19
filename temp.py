from dash import Dash, dcc, html
from dash.dependencies import Input, Output

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='my-input', value='初始值', type='text'),
    html.Div(id='my-output')
])

@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='my-input', component_property='value')]
)
def update_output_div(input_value):
    return f'您輸入了: {input_value}'

if __name__ == '__main__':
    app.run_server(debug=True)
