import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np


app = dash.Dash(__name__)

#plotly scatter figure
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=np.random.randint(1,50,40),
    y=np.random.randint(1,60,40),
    mode="markers"    
))

app.layout = html.Div([

    html.Div([

    html.H1("Css Header"),
    html.P("""
        Hi There. This is a sample paragraph for working with css
    """)
    ],className="container"),

    dcc.Graph(
        id="random-scatter-graph",
        figure=fig)
])

if __name__ == "__main__":
    app.run_server()