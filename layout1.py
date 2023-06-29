import dash
from dash import Dash,html,dcc,Input,Output,callback

app=Dash(__name__)

app.layout=html.Div([
    dcc.Location(id='url',refresh=False),
    html.Div(id='page-content')
        ])