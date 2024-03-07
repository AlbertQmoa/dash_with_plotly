
'''
    reference: https://www.youtube.com/watch?v=7m0Bq1EGPPg&t=795s
'''

from dash import Dash, dcc, Output, Input  
import dash_bootstrap_components as dbc
import plotly.express as px


#  ========== incorporate data into app ==========
df = px.data.medals_long()


# ========== Build your components ==========
app = Dash(__name__, external_stylesheets=[dbc.themes.VAPOR])
mytitle = dcc.Markdown(children='# App that analyzes Olympic medals')
mygraph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=['Bar Plot', 'Scatter Plot'],
                        value='Bar Plot',  # initial value displayed when page first loads
                        clearable=False)
    # mytitle 是一個 Markdown 組件，顯示了應用的標題。
    # mygraph 是一個圖表組件，初始時沒有圖形，將用於顯示用戶選擇的數據可視化。
    # dropdown 是一個下拉選單組件，讓用戶選擇是查看條形圖還是散點圖。


# ========== Customize your own Layout ==========
app.layout = dbc.Container([mytitle, mygraph, dropdown])
    # app.layout 使用 dbc.Container 將標題、圖表和下拉選單組織到一個容器中，這將是網頁的主要佈局。 


# ========== Callback allows components to interact ==========
@app.callback(
    Output(mygraph, component_property='figure'),
    Input(dropdown, component_property='value')
)
def update_graph(user_input):  # function arguments come from the component property of the Input
    if user_input == 'Bar Plot':
        fig = px.bar(data_frame=df, x="nation", y="count", color="medal")

    elif user_input == 'Scatter Plot':
        fig = px.scatter(data_frame=df, x="count", y="nation", color="medal",
                         symbol="medal")

    return fig  # returned objects are assigned to the component property of the Output


# ========== Run app ==========
if __name__=='__main__':
    app.run_server(port=8053)