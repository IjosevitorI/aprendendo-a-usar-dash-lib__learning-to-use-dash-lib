from dash import Dash, State, dcc, html, Input, Output, callback
import pandas as pd
import plotly.express as px
from io import StringIO

# 1. BLOCO DE DADOS
def carregar_e_tratar_dados():
#Lê a string de dados, interpola valores nulos e calcula médias.
    dados = """data, temperatura_c, nivel_rio_m, ndvi
    2025-01-01, 32.5, 4.2, 0.65
    2025-01-02, 33.1, 4.3, 0.67
    2025-01-03, 34.0, , 0.66
    2025-01-04, 35.2, 4.5,
    2025-01-05, 36.0, 4.7, 0.70
    2025-01-06, 35.5, 4.8, 0.72
    2025-01-07, 34.8, , 0.71
    2025-01-08, 33.9, 4.6, 0.69
    2025-01-09, 32.7, 4.4,
    2025-01-10, 31.8, 4.3, 0.66"""

    df = pd.read_csv(StringIO(dados), sep=',', skipinitialspace=True)
    df['data'] = pd.to_datetime(df['data'])

    df_tratado = df.copy()
    df_tratado['nivel_rio_m'] = df_tratado['nivel_rio_m'].interpolate(method='linear')
    df_tratado['ndvi'] = df_tratado['ndvi'].interpolate(method='linear')

    medias = df_tratado.mean(numeric_only=True)

    return df_tratado, medias



# 2. BLOCO DE VISUALIZAÇÃO (LAYOUT)
def criar_layout():
#Constrói e retorna a estrutura visual da Visualização.

    texto_cabecalho = """
    # 📊 Monitoramento Ambiental 
    *Nota: Dados ausentes foram preenchidos por interpolação linear.*
    """

    return html.Div([
        dcc.Markdown(texto_cabecalho),

        html.Label("Métrica para Visualizar no Gráfico:"),
        dcc.Dropdown(id='metricas-dropdown', options=[
            {'label': 'Temperatura (°C)', 'value': 'temperatura_c'},
            {'label': 'Nível do Rio (m)', 'value': 'nivel_rio_m'},
            {'label': 'NDVI', 'value': 'ndvi'}
        ], value='temperatura_c', style={'marginBottom': '20px'}),

        dcc.Graph(id='grafico-metricas'),

        html.Hr(),

        html.H3("Exportar e Imprimir Dados"),
        html.Label("Escolha como ordenar a tabela:"),
        dcc.Dropdown(id='ordenacao-dropdown', options=[
            {'label': 'Ordem Cronológica (Data)', 'value': 'data'},
            {'label': 'Temperatura (Crescente)', 'value': 'temperatura_c'},
            {'label': 'Nível do Rio (Crescente)', 'value': 'nivel_rio_m'},
            {'label': 'NDVI (Crescente)', 'value': 'ndvi'}
        ], value='data', style={'marginBottom': '10px'}),

        html.Button('Gerar CSV e Imprimir na Tela', id='botao-exportar', n_clicks=0, 
                    style={'padding': '10px', 'backgroundColor': '#595959', 'color': 'white', 'border': 'none', 'cursor': 'pointer'}),
    

        html.Div(id='mensagem-exportacao', style={'marginTop': '15px', 'fontWeight': 'bold', 'color': 'green'})

    ], style={'font-family': 'Arial, sans-serif', 'maxWidth': '900px', 'margin': '0 auto', 'padding': '20px'})



# 3. BLOCO DE CONTROLE (CALLBACKS)
def registrar_callbacks(app, df_tratado, medias):
#Registra todas as interações dinâmicas da visualização.


    @app.callback(
        Output('grafico-metricas', 'figure'),
        Input('metricas-dropdown', 'value')
    )
    def atualizar_grafico(metrica):
        valor_media = medias[metrica]

        fig = px.line(
            df_tratado,
            x='data',
            y=metrica,
            title=f'{metrica} ao longo do tempo',
            template='plotly_white',
            color_discrete_sequence=['#595959']
        )

        fig.add_scatter(
            x=[df_tratado['data'].min(), df_tratado['data'].max()],
            y=[valor_media, valor_media],
            mode='lines',
            name='Valor Médio',
            line=dict(color='#A6A6A6', dash='dash', width=2),
            hoverinfo='name+y'
        )

        fig.update_traces(line=dict(width=3), selector=dict(mode='lines', name=metrica))
        return fig

    @app.callback(
        Output('mensagem-exportacao', 'children'),
        Input('botao-exportar', 'n_clicks'),
        State('ordenacao-dropdown', 'value'),
        prevent_initial_call=True
    )
    def exportar_dados(n_clicks, criterio_ordenacao):
        df_ordenado = df_tratado.sort_values(by=criterio_ordenacao)

        print(f"\n--- Tabela Ordenada por: {criterio_ordenacao} ---")
        print(df_ordenado.to_string(index=False))
        print("----------------------------------------\n")

        nome_arquivo = f"dados_ordenados_{criterio_ordenacao}.csv"
        df_ordenado.to_csv(nome_arquivo, index=False)

        return f"Arquivo '{nome_arquivo}' foi gerado na sua pasta e os dados foram impressos no terminal."



# 4. BLOCO DE EXECUÇÃO
if __name__ == '__main__':
    # 1. Prepara os dados
    df, medias_df = carregar_e_tratar_dados()

    # 2. Inicializa o App
    app = Dash(__name__)

    # 3. Constroi a interface visual
    app.layout = criar_layout()

    # 4. Conecta Callbacks
    registrar_callbacks(app, df, medias_df)

    # 5. Roda o App
    app.run(debug=True)