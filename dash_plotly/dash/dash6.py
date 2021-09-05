import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([

    html.H2("Text Box"),
    dcc.Input(
        type='text',
        placeholder="Enter Your Name here"
    ),

    html.H2("Text Area"),
    dcc.Textarea(
        placeholder="Enter a description",
        style={
            "height":"5em"
        }
    ),
    html.H2("Checkbox"),
    dcc.Checklist(
        options=[
            {"label":"Haikyuu","value":"haikyuu"},
            {"label":"kuroko no basket","value":"Kuroko no basket"},
            {"label":"hajime no ippo","value":"hajime no ippo"}
        ],
        value=["Kuroko no basket"]
    ),
    html.H2("Radio Button"),
    dcc.RadioItems(
        options=[
            {"label":"Haikyuu","value":"haikyuu"},
            {"label":"kuroko no basket","value":"Kuroko no basket"},
            {"label":"hajime no ippo","value":"hajime no ippo"}
        ],
        value='haikyuu'
    )
])


if __name__ == "__main__":
    app.run_server()