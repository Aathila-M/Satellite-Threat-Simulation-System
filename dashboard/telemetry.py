import plotly.graph_objects as go
import random

def telemetry_graph():

    signal = [random.randint(40,100) for i in range(10)]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        y=signal,
        mode='lines+markers',
        name="Signal Strength"
    ))

    fig.update_layout(
        title="Live Satellite Telemetry",
        xaxis_title="Time",
        yaxis_title="Signal Strength"
    )

    return fig.to_html(full_html=False)