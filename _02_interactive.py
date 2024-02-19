from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc

# ====== Build your components ======
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
mytext = dcc.Markdown(children='')
myinput = dbc.Input(value="# Hello World - let's build web apps in Python!")


# ====== Customize your own Layout ======
app.layout = dbc.Container([mytext, myinput])
    # 這行代碼的作用是將 mytext 和 myinput 兩個 Dash 組件作為子組件放入 dbc.Container 容器中。
    # 這樣做的結果是在網頁上創建了一個容器，容器中有文字和輸入框。
    # 这些组件将按照列表中的順序（在这个例子中是 mytext 紧接着 myinput）被垂直排列显示。


# ====== Callback allows components to interact ======
@app.callback(
    Output(mytext, component_property='children'),
    Input(myinput, component_property='value')
)
def update_title(user_input):   # *** function arguments come from the component property of the Input
    return user_input           # *** returned objects are assigned to the component property of the Output
                                # 多個 Iuputs 代表你要輸入相對多的 arguments。同理 for Outputs。


# ====== Run app ======
if __name__=='__main__':
    app.run_server(port=8052)