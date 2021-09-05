import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State

app = dash.Dash()


app.layout = html.Div([

    html.H2("Checkbox"),
    dcc.Input(
        id="input-text",
        type="text",
        value=" "
    ),
    html.Button(
        id="submit-button",
        n_clicks=0,
        children="Submit"
    ),
    html.P(
        id="paragraph"
    )
])

@app.callback(
    Output("paragraph","children"),
    [Input("submit-button","n_clicks")],
    [State("input-text","value")]
)
def update_para(but_click,inp_val):
    return f"{inp_val} is your favourite"

if __name__ == "__main__":
    app.run_server()