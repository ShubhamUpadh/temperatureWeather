import dash
import csv
import dash_bootstrap_components as dbc
from dash import html, Input, Output, dcc
from datetime import datetime
import requests

colors = {
    'background': '#000000'
}

borderInf = {
    'Inf': '5px solid gray',
    'Inf1': '1px #898989'
}

textCol = {
    'text': '#FFF'
}


def fxtempReturn(city):
    baseUrl = "https://api.openweathermap.org/data/2.5/weather?"
    apikey = open('apikey.txt', 'r').read()
    url = baseUrl + "appid=" + apikey + "&q=" + city
    response = requests.get(url).json()
    return response


def fxfactsAPI():

    api_url = 'https://api.api-ninjas.com/v1/facts?limit=1'

    apikeyFacts = open('apikeyfacts.txt', 'r').read()
    response = requests.get(api_url, headers={apikeyFacts: 'YOUR_API_KEY'})
    print(response)

    if response.status_code == requests.codes.ok:
        return response.text
    else:
        return "Police detectives have used snapping turtles to help them locate dead bodies", response.status_code, response.text


def fxgreetMsg():
    now = datetime.now()

    if 5 < int(now.hour) < 12:
        return "Morning"
    elif 11 < int(now.hour) < 17:
        return "Afternoon"
    else:
        return "Evening"


greetMsg = fxgreetMsg()
# print(fxtempReturn("Delhi"))

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.title = "Tempteller"

app.layout = html.Div(style={'paddingTop': 50}, children=[

    dbc.Container([

        dbc.Row([
            html.Div(html.B(f"Hi, Good {greetMsg}"), style={'fontSize': 40, 'color': '#000', 'textAlign': 'left',
                                                            'marginBottom': 40})

        ]),

        dbc.Row([
            html.Div(html.B(fxfactsAPI()[0]),
                     style={'fontSize': 25, 'color': '#000', 'textAlign': 'center',
                            'marginBottom': 10})

        ]),

        dbc.Row([html.Div(html.B("-Just a random fact-"),
                          style={'fontSize': 15, 'color': '#000', 'textAlign': 'right',
                                 'marginBottom': 20})
                 ]),

        html.Hr(style={'color': '#FFF'}),



        dbc.Row(children=[
            dbc.Col(width=4),
            dbc.Col(
                [html.Div(
                    dcc.Dropdown(
                        options=[
                            {'label': 'Delhi', 'value': 'Delhi'},
                            {'label': 'Ghaziabad', 'value': 'Ghaziabad'},
                            {'label': 'Bangalore', 'value': 'Bengaluru'},
                            {'label': 'Melbourne', 'value': 'Melbourne, AU'},

                        ],
                        value="Delhi", placeholder="Select a city",
                        id="demo-dropdown"
                    ),
                )
                ], width=4),
            dbc.Col(width=4)
        ]),

        html.Br(),

        dbc.Row([html.Div(html.B(id='dd-output-container'),
                          style={'marginTop': 10, 'marginBottom': 15, 'textAlign': 'center', 'fontSize': 20,
                                 'color': '#000'})
                 ]),

        html.Hr(style={'color': '#FFF'})

    ])

])


@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
)
def update_output_div(input_value):
    if input_value is None:
        return "Weather stats of the selected city will appear here"

    res = fxtempReturn(input_value)

    return (
        f"In {input_value}, current temperature is {str(res['main']['temp'] - 273.15)[0:5]} C. The humidity is {res['main']['humidity']} %"
        f" and the current wind speed is {res['wind']['speed']}")


if __name__ == "__main__":
    app.run_server(debug=True)
