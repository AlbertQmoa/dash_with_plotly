from dash import Dash, dcc
import dash_bootstrap_components as dbc
    # Dash 是創建應用的主類別。
    # dcc（Dash Core Components）包含了一系列可以在 Dash 應用中使用的組件，如圖表、滑動條等。
    # dbc（Dash Bootstrap Components）提供了一套基於 Bootstrap 的組件，便於快速創建美觀的佈局和元素。


# ====== Build your components ======
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    # 這行代碼初始化了一個 Dash 應用實例，並透過 external_stylesheets 參數引入了 Bootstrap 主題樣式。
    # 這樣，你就可以利用 Bootstrap 的樣式來美化你的 Dash 應用。
mytext = dcc.Markdown(children="# Hello World - let's build web apps in Python!")
    # 這裡使用了 Dash Core Components 中的 Markdown 組件來創建一個 Markdown 文本，children 屬性定義了組件的內容。
    # 這段 Markdown 文本簡單地展示了一級標題 "Hello World - let's build web apps in Python!"。
    # 在 Dash 和許多其他前端框架中，children 屬性是一個非常重要的概念。
    # 它用於指定一個組件內部包含的內容或子組件。簡單來說，children 屬性定義了該組件應當渲染的內容，這些內容可以是文本、數據、甚至是其他更複雜的組件。


# ====== Customize your own Layout ======
app.layout = dbc.Container([mytext])
    # 應用的佈局（app.layout）被設置為一個 dbc.Container，這是 Dash Bootstrap Components 提供的一個容器組件，用於包含和組織其他組件。
    # 這裡，它包含了之前創建的 Markdown 組件 mytext。


# Run app
if __name__=='__main__':
    app.run_server(port=8051)