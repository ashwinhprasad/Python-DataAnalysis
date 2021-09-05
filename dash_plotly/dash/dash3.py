# styling
import dash
import dash_html_components as html
import dash_core_components as dcc


app = dash.Dash()

app.layout = html.Div([

    html.H1(children = "Hello Dash!!",style = {
        'textAlign':'center',
        'color':'steelblue'
    }),
    dcc.Graph(
        id='sample-graph',
        figure = {
            'data': [
                { "x": [1,2,3],"y": [12,14,5],'type':'bar','name':'First chart' },
                { "x":[1,2,3], "y":[20,12,21], "type":'bar', 'name':'Second chart'}
            ],
            'layout':{
                'title':'Simple bar chart',
                'plot_bgcolor':'black',
                'paper_bgcolor':'black',
                'font':{
                   'color':'white'
                }

            },
        },
    )

])


if __name__ == "__main__":
    app.run_server(port=8050)
