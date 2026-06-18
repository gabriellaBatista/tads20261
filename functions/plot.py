import plotly.express as px
from plotly.graph_objects import Figure
from functions.data import download_history

download_history('BBAS3.SA')


def plot_history(ticker:str) ->Figure:
    df = download_history(ticker)

    fig = px.line(
        df,
        x= 'Date' ,
        y= 'Close' ,
        title = f'{ticker} stock price.'
    )

    return fig