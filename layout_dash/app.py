from container import container_main, app

# cria o layout da página
app.layout = container_main


# executor do modulo objeto Dash
app.run(debug=True)

