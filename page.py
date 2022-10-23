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
    city = "Delhi"
    url = baseUrl + "appid=" + apikey + "&q=" + city
    response = requests.get(url).json()
    return response


def fxfactsAPI():
    limit = 1
    api_url = 'https://api.api-ninjas.com/v1/facts?limit={1}'

    apikeyFacts = open('apikeyfacts.txt', 'r').read()
    response = requests.get(api_url, headers={apikeyFacts: 'YOUR_API_KEY'})

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
print(fxtempReturn("Delhi"))

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

        dbc.Row([html.Div(html.B("I will tell you the longest english dictionary word that doesn't contain the "
                                 "entered alphabets."),
                          style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                                 'marginBottom': 20})
                 ]),

        dbc.Row([html.Div(html.B("For example, the longest dictionary word that doesn't contain the alphabets (a, x, i,"
                                 " s) is HYDROMETEOROLOGY."),
                          style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                                 'marginBottom': 30, 'marginTop': 30})
                 ]),

        html.Hr(style={'color': '#FFF'}),

        dbc.Row([html.Div(html.B("Enter the alphabets that the word SHOULD NOT contain : "),
                          style={'fontSize': 20, 'color': '#FFF', 'textAlign': 'center',
                                 'marginBottom': 5, 'marginTop': 15})
                 ]),

        dbc.Row(
            [html.Div(dcc.Input(id='my-input', value='', type='text'),
                      style={'marginTop': 0, 'textAlign': 'center', 'fontSize': 20, 'color': '#FFF'})
             ]),

        html.Br(),

        dbc.Row([html.Div(html.B(id='my-output'),
                          style={'marginTop': 10, 'marginBottom': 15, 'textAlign': 'center', 'fontSize': 20,
                                 'color': '#FFF'})
                 ]),

        html.Hr(style={'color': '#FFF'})

    ])

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    '''check = True

    if len(input_value) == 0:
        return "NO INPUT DETECTED"
    z = list()
    for alpha in input_value:
        if alpha.isalpha() and not alpha in z:
            z.append(alpha)
            check = False

    if check:
        return "NO INPUT DETECTED"

    print(z)

    lenWord = 0
    longestWord = ""

    with open("dictionaryPreprocessed.csv", mode='r') as file:
        fileF = csv.reader(file)
        for lines in fileF:

            flag = True

            for alphabet in z:
                if alphabet.lower() in str(lines) or alphabet.upper() in str(lines):
                    flag = False
                    break

            if flag and lenWord < len(str(lines)) and not " " in str(lines):
                longestWord = str(lines)
                lenWord = len(str(lines))

    if longestWord == "" or len(longestWord) == 5:
        return "No such word exists :( "

    elif input_value in ('Bijoy', 'bijoy'):
        return "BIJOY JADAV"

    elif input_value == 'Vivek':
        return "MANAGER MARAJ"

    else:
        return str(longestWord[2:-2]).upper()'''

    return "HELLO"


if __name__ == "__main__":
    app.run_server(debug=True)
