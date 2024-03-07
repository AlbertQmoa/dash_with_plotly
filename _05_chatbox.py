import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# 在外部定义组件
chat_history_store = dcc.Store(id='chat-history')
chat_box_div = html.Div(id='chat-box', style={'overflow': 'auto', 'max-height': '75vh', 'padding-bottom': '20px'})
user_input_textarea = dcc.Textarea(id='user-input', style={'width': '100%', 'height': '150px'}, placeholder="请输入内容...")
send_button = html.Button("发送", id="send-button", n_clicks=0, className="btn btn-primary mt-2")
input_div = html.Div([user_input_textarea, send_button], 
                     style={'position': 'fixed', 'bottom': 0, 'left': 0, 'right': 0, 'padding': '10px', 'background': 'white'})

# 使用外部定义的组件构建layout
app.layout = html.Div([
    chat_history_store,
    chat_box_div,
    input_div
], style={'padding': '10px'})

def generate_plot_response():
    # 创建散点图数据
    df = pd.DataFrame({
        "x": [1, 2, 3, 4, 5],
        "y": [2, 1, 4, 3, 5]
    })
    fig = px.scatter(df, x="x", y="y")
    plot_response = dcc.Graph(figure=fig)
    return plot_response

@app.callback(
    Output('chat-box', 'children'),
    Output('user-input', 'value'),
    Input('send-button', 'n_clicks'),
    State('user-input', 'value'),
    State('chat-history', 'data'),
)
def update_chat(n_clicks, user_input, chat_history):
    if n_clicks > 0 and user_input:
        if chat_history is None:
            chat_history = []

        # 将用户输入的内容添加到聊天历史中
        chat_history.append({'sender': 'User', 'message': user_input})

        # 简单地反转用户输入作为服务器响应
        server_response = f"Server response: {user_input[::-1]}"
        chat_history.append({'sender': 'Server', 'message': server_response})
        
        # 假设根据某些条件服务器决定发送一个散点图
        if "plot" in user_input:
            plot_response = generate_plot_response()
            chat_history.append({'sender': 'Server', 'type': 'plot', 'content': plot_response})
        
        # 将服务器的文字响应添加到聊天历史中
        
        user_input = ''  # 清空输入框
        chat_content = []

        # 遍历聊天历史并按照顺序构建聊天内容
        for msg in chat_history:
            chat_content.append(html.Div([
                html.B(f"{msg['sender']}:", style={'color': '#007BFF' if msg['sender'] == 'User' else '#FF5733'}),
                msg['content'] if msg.get('type') == 'plot' else html.Pre(msg['message'], style={'white-space': 'pre-wrap', 'margin-left': '20px'}),
            ], style={'margin-bottom': '15px'}))

        return chat_content, user_input
    return dash.no_update

if __name__ == '__main__':
    app.run_server(debug=True)
