# intro

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.H1("Hello Dash"),
    html.Div("Dash - a data product development framework from plotly")
])

if __name__ == "__main__":
    app.run_server(port=8050)
