from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from handle_data import stations_list
from dash import Dash

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP] , suppress_callback_exceptions=True)

@app.callback(
    Output('estacao-dropdown', 'options'),
    Input('estado-dropdown','value')
)
def update_dropdown_stations(selected_estado):
    stations = stations_list(selected_estado)
    return stations


if __name__ == '__main__':
    estacoes = stations_list('AM')
    print(estacoes)
    
