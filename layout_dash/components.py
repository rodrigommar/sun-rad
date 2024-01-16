import dash_bootstrap_components as dbc
from dash import html, dcc


# It's creating search component
search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Pesquisar")),
        dbc.Col(dbc.Button("Pesquisar", color="primary", className="ms-2", n_clicks=0), width="auto",),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)


# It's creating Navbar component
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="https://images.plot.ly/logo/new-branding/plotly-logomark.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("ORION - Dashboard Clima", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="http://127.0.0.1:8050/",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                search_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
)


# Card destinado a integrar o formulário de pesquisa das estações
# create list of states and stations
#lista_estados = states_list()
#lista_estacoes = stations_list(df_stations, sg_state=None)

stations_card = dbc.Card(
    [ 
        dbc.CardHeader("Selecione a estação"),
        html.Div(
            children=[
                html.Form(
                    [
                        html.Fieldset(
                            [
                                html.Div(
                                    className="form-group", 
                                    children=[
                                        html.Label(
                                            "Estado",
                                            className="form-label mt-4"
                                        ),
                                        dcc.Dropdown(
                                            options=[
                                                {
                                                    "label": 'estado',
                                                    "value": 'estado'
                                                }
                                                for estado in 'lista_estados'
                                            ],
                                            id="estado-dropdown",
                                            #value=lista_estados[0]
                                        ),
                                    ]
                                ),
                                html.Div(
                                    className="form-group",
                                    children=[
                                        html.Label(
                                            "Estação",
                                            className="form-label mt-4"
                                        ),
                                        dcc.Dropdown(
                                            options=[
                                                {
                                                    "label": 'estacao',
                                                    "value": 'estacao'
                                                }
                                            ],
                                            id="estacao-dropdown",
                                            #value=lista_estacoes
                                        )
                                    ]
                                ),
                                html.Div(children=[html.P('') ],id='pula_linha'), # Pula uma linha
                                html.Div(
                                    [
                                        dcc.RadioItems(
                                            ['Mês', 'Dia', 'Periodo'],
                                            'Dia',
                                            id='radio-input-date',
                                            inline=True,
                                        ),
                                        html.P(''), # Pula uma linha
                                        dcc.Store(id='period-store',data=None),
                                        dcc.Store(id='day-store',data=None),
                                        dcc.Store(id='month-store',data=None),                                       
                                        dcc.Loading([html.Div(id='loading-demo')])
                                    ]
                                ),
                                html.P(''),
                                dbc.Button("Limpar", id="reset-button", color="primary", className="ms-2", n_clicks=0)
                            ]
                        ),
                    ],
                    id="form_main"
                ),
            ]
        )
    ]
)

"""  
@app.callback(
    Output('estacao-dropdown', 'options'),
    Input('estado-dropdown','value')
)
def update_dropdown_stations(selected_estado):
    print(selected_estado)
    

if __name__ == '__main__':
    print(update_dropdown_stations()) """