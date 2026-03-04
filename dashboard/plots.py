import pandas as pd
import plotly.express as px

def attack_pie():

    df = pd.read_csv("dataset/synthetic_satellite_data.csv")

    fig = px.pie(
        df,
        names="attack_type",
        title="Satellite Attack Distribution"
    )

    return fig.to_html(full_html=False)