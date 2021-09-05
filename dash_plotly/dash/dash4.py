# scatterplot

import numpy as np
import dash
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc

x = np.random.randint(1,60,60)
y = np.random.randint(1,60,60)

app = dash.Dash()

app.layout = html.Div([

    dcc.Graph(
        id="scatterplot",
        figure = {
            'data':[
                go.Scatter(
                    x=x,y=y,mode='markers'
                )
            ],
            'layout':go.Layout(
                title="Scatter of 80 random plots",
                xaxis={ 'title':'random X values'},
                yaxis={'title':'random Y values'},
                plot_bgcolor='black',
                paper_bgcolor="black",
                font={
                    'color':"white"
                }
            )
        }
    )
])


if __name__ == "__main__":
    app.run_server(port=8050)