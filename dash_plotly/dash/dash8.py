import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State

app = dash.Dash()


app.layout = html.Div([

    html.H2("Checkbox"),
    dcc.RadioItems(
        id="radio",
        options=[
            {"label":"Haikyuu","value":"haikyuu"},
            {"label":"kuroko no basket","value":"Kuroko no basket"},
            {"label":"hajime no ippo","value":"hajime no ippo"}
        ],
        value="Kuroko no basket"
    ),
    html.P(
        id="paragraph"
    )
])

@app.callback(
    Output("paragraph","children"),
    [Input("radio","value")],
)
def update_para(value):
    return f"{value} is your favourite"

if __name__ == "__main__":
    app.run_server()