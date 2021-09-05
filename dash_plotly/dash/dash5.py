# importing the libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd

# creating Dash instance
app = dash.Dash()

app.layout = html.Div([

    html.H1("DropDown and Slider Tutorial"),

    dcc.Dropdown(
        id="Dropdown Sample",
        options = [
            {"label":"Logistic Regression","value":"Logistic Regression"},
            {"label":"Linear Regression","value":"Linear Regression"},
            {"label":"Decision Tree","value":"Decision Tree"}
        ],
        placeholder="Select an Algorithm"
    ),

    html.Br(),
    html.H2(children="Slider",style={
        "textAlign":"center"
    }),
    dcc.Slider(
        min=0,
        max=10,
        value=5,
        step=0.1,
        marks=[i for i in range(10)]
    ),
    html.H2(children="Range Slider",style={
        "textAlign":"center"
    }),

    dcc.RangeSlider(
        min=0,
        max=10,
        value=[3,7],
        marks=[i for i in range(10)]
    )

])

# run server
if __name__ == "__main__":
    app.run_server()