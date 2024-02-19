

# =========================================== 基本概念 ===========================================
# Dash 的基本組成
    Dash 是由 Plotly 提供的一個 Python 框架，用於構建網頁分析應用程式。Dash 應用程式由三大核心部分組成：Component（組件）、Layout（佈局）和 Callback（回調）。下面將分別對這三部分進行介紹：

    Component（組件）
        Dash 組件是構建應用程式用戶界面（UI）的樂高積木。這些組件代表了 HTML 的所有基本元素，如 div、span、a 等，以及更高級的組件，如圖表、表格、下拉菜單等。Dash 提供了兩大組件庫：
            dash_html_components：這個庫包含了一套與 HTML 元素一一對應的 Python 組件，用於創建標準的 HTML 內容。
            dash_core_components：這個庫提供了一些更高級的組件，比如圖表（透過 Plotly）、日期選擇器、滑動條等，這些都是互動式組件，用戶可以通過操作這些組件來與 Dash 應用程式互動。

    Layout（佈局）
        Layout 定義了應用程式的外觀和感覺。在 Dash 中，佈局是通過組合組件來構建的，並且是以 Python 的方式進行描述。
        你可以使用 div 組件來創建容器，並將其他組件作為子元素放入這些容器中，從而形成整個應用的結構。
        Layout 是一個 Python 對象，通常會賦值給 app.layout 屬性。
    
    Callback（回調）
        Callback 創建了應用程式的互動性，它是 Dash 應用程式的靈魂。
        通過定義回調函數，你可以指定 UI 組件的哪些互動操作（例如點擊按鈕、選擇下拉菜單項）會觸發應用程式的哪些 Python 函數，以及這些 Python 函數將如何修改應用程式的狀態或外觀。
        回調函數至少需要兩個裝飾器參數：
            Output：定義了函數執行結果的目的地，即哪個組件的哪個屬性會被更新。
            Input：指定了觸發回調函數的事件，即哪個組件的哪個行為（例如點擊或選擇）會觸發函數。
        此外，回調還可以有可選的 State 參數，它允許函數讀取但不監控某些 UI 元素的狀態。


# Dash 的疊加
    在 Dash 這類 Web 應用框架中，「疊加」概念是通過 children 屬性來實現的，這裡我們將其相關的知識點做一個整理：
    
    children 屬性的角色
        層次結構的基礎：children 屬性允許開發者按照層次結構來組織應用界面中的元素。
        這種層次結構類似於一棵樹，其中容器組件作為父節點，而放置在其中的內容或子組件則是其子節點。
        組件疊加：透過在父組件的 children 屬性中放置一個或多個子組件，可以實現組件的「疊加」，形成豐富且結構化的用戶界面。
        children 可以再有 children，可以一直疊下去。

    children 屬性的示例
        假設我們想在一個 Dash 應用中創建一個包含標題、圖表和說明文本的面板，我們可以這樣做：
            import dash_html_components as html
            import dash_core_components as dcc

            app.layout = html.Div(children=[
                html.H1(children='這是標題'),
                dcc.Graph(id='example-graph', figure=...),
                html.P(children='這裡是對圖表的說明文本。')
            ])
        在這個示例中，html.Div 是最外層的容器組件，其 children 屬性中包含了三個子組件：一個 html.H1 標題組件、一個 dcc.Graph 圖表組件和一個 html.P 文本組件。這些子組件按照給定的順序被「疊加」在一起，形成了一個結構化且層次分明的界面。



# =========================================== Component ===========================================


# =========================================== Layout ===========================================


# =========================================== Callback ===========================================
# Input & Output
    概念：
        在 Dash 中，Input 和 Output 是構建互動式應用的基石，它們定義了應用中元素之間的互動方式。
        這些元素可以是用戶界面的一部分，如輸入框、滑動條或按鈕，也可以是顯示資料的圖表或文本。
        Input 和 Output 通過回調（Callbacks）機制連接在一起，使得 Dash 應用能夠根據用戶的互動動態更新內容。
    Input：
        Input 物件定義了回調函數的觸發條件。每當定義為 Input 的組件的特定屬性發生變化時（例如，用戶在輸入框中輸入文本，或是用戶選擇了下拉菜單中的一個選項），相關聯的回調函數就會被觸發執行。
        Input 的 component_property 是說 component_id 這個物件的哪個部分有變化時要觸發callback函數
            [Input(component_id='my-input', component_property='value')]
        當你的回調函數需要根據多個不同組件的狀態變化來執行時，你可以將多個 Input 物件放在列表中。這樣，任何一個 Input 中指定的組件屬性發生變化時，都會觸發該回調函數執行。
        為什麼即使是單個輸入也要使用列表?
            即便是單個 Input，將其寫在列表中也是一種慣用法。這主要是為了保持一致性和擴展性，當你需要增加更多的輸入時，只需要在列表中添加新的 Input 物件即可，而不需要修改回調函數的結構或語法。這樣做提高了代碼的可維護性和可讀性。
    Output：
        Output 物件定義了回調函數執行後將要更新的組件屬性。當回調函數被觸發並執行後，它將產生一些輸出，這些輸出會被用來更新一個或多個組件的指定屬性（例如，更新一個文本元素來顯示最新計算的結果，或是更新一個圖表的數據源）。
        Ouput 的 component_property 是說 component_id 這個物件的哪個部分要被更新
            Output(component_id='my-output', component_property='children')
    回調（Callbacks）
        在 Dash 中，回調函數是通過裝飾器 @app.callback 定義的，它將一個或多個 Input 物件和一個或多個 Output 物件關聯起來。這個函數的主體定義了當輸入值變化時應當執行的操作，以及如何計算新的輸出值。
    示例：
        假設我們有一個簡單的 Dash 應用，包括一個輸入框和一個文本顯示元素。用戶在輸入框中輸入文本後，下方的文本顯示元素會更新為輸入框中的內容。
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
        在這個例子中，dcc.Input 組件的 value 屬性被定義為一個 Input，而 html.Div 組件的 children 屬性則被定義為一個 Output。當用戶在輸入框中輸入文字時，回調函數 update_output_div 會被觸發，並使用用戶輸入的內容來更新下方 Div 中的文本。
        