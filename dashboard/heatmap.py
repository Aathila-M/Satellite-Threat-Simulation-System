import pandas as pd
import plotly.express as px

def signal_heatmap():

    df = pd.read_csv("dataset/synthetic_satellite_data.csv")

    fig = px.density_heatmap(
        df,
        x="signal_strength",
        y="latency",
        title="Satellite Signal Heatmap"
    )

    return fig.to_html(full_html=False)