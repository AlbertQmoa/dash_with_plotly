'''
    Code is copied from [All about the Graph Component - Python Dash Plotly](https://youtu.be/G8r2BB3GFVY)
    Used for self-study only
'''
import dash
from dash import dcc, html, Output, Input
import plotly.express as px

df = px.data.gapminder()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# external_stylesheets = ['./style.css']
    # 在Dash應用中，external_stylesheets變量用於引入外部CSS樣式表，這樣可以為你的應用添加預定義的樣式。
    # 這種方法使得開發者能夠輕鬆地定製和改善應用的外觀和用戶體驗。

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# ====================================== Componets & Layout ======================================
app.layout = html.Div([
    dcc.Dropdown(id='dpdn2', value=['Germany','Brazil'], multi=True,
                 options=[{'label': x, 'value': x} for x in df.country.unique()]),
        # id='dpdn2'：這是下拉選單的唯一標識符（ID），用於在Dash應用中引用這個特定的下拉選單。
        # value=['Germany','Brazil']：這指定了下拉選單的初始選中值。在這個例子中，下拉選單一開始會選中德國（Germany）和巴西（Brazil）這兩個國家。
        # multi=True：這表示下拉選單允許多選。用戶可以選擇一個或多個選項。
        # options=[{'label': x, 'value': x} for x in df.country.unique()]：這行代碼生成了下拉選單的選項列表。
        # 它迭代了df.country.unique()返回的所有唯一國家名稱，每個國家名稱x都會生成一個字典，其中包含兩個鍵值對：'label': x和'value': x。
        # label是在下拉選單中顯示給用戶看的文本，value是當選項被選中時，相應選項的值。這意味著下拉選單的選項將來自於df這個DataFrame中country列的所有唯一值。

    html.Div([
        dcc.Graph(id='pie-graph', figure={}, className='six columns'),
        dcc.Graph(id='my-graph', figure={}, clickData=None, hoverData=None, # I assigned None for tutorial purposes. By defualt, these are None, unless you specify otherwise.
                  config={
                      'staticPlot': False,     # True, False
                      'scrollZoom': True,      # True, False
                      'doubleClick': 'reset',  # 'reset', 'autosize' or 'reset+autosize', False
                      'showTips': False,       # True, False
                      'displayModeBar': True,  # True, False, 'hover'
                      'watermark': True,
                      # 'modeBarButtonsToRemove': ['pan2d','select2d'],
                        },
                  className='six columns'
                  )
    ])
])


# ====================================== Callbacks ======================================
@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='dpdn2', component_property='value'),
)
def update_graph(country_chosen):
    dff = df[df.country.isin(country_chosen)]
    fig = px.line(data_frame=dff, x='year', y='gdpPercap', color='country',
                  custom_data=['country', 'continent', 'lifeExp', 'pop'])
    fig.update_traces(mode='lines+markers')
    return fig


# Dash version 1.16.0 or higher
@app.callback(
    Output(component_id='pie-graph', component_property='figure'),
    Input(component_id='my-graph', component_property='hoverData'),
    Input(component_id='my-graph', component_property='clickData'),
    Input(component_id='my-graph', component_property='selectedData'),
    Input(component_id='dpdn2', component_property='value')
)
def update_side_graph(hov_data, clk_data, slct_data, country_chosen):
    if hov_data is None:
        dff2 = df[df.country.isin(country_chosen)]
        dff2 = dff2[dff2.year == 1952]
        print(dff2)
        fig2 = px.pie(data_frame=dff2, values='pop', names='country',
                      title='Population for 1952')
        return fig2
    else:
        print(f'hover data: {hov_data}')
        # print(hov_data['points'][0]['customdata'][0])
        # print(f'click data: {clk_data}')
        # print(f'selected data: {slct_data}')
        dff2 = df[df.country.isin(country_chosen)]
        hov_year = hov_data['points'][0]['x']
        dff2 = dff2[dff2.year == hov_year]
        fig2 = px.pie(data_frame=dff2, values='pop', names='country', title=f'Population for: {hov_year}')
        return fig2


if __name__ == '__main__':
    app.run_server(debug=True)