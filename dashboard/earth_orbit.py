import plotly.graph_objects as go
import numpy as np

def earth_orbit():

    t = np.linspace(0,2*np.pi,100)

    x = np.cos(t)
    y = np.sin(t)
    z = 0.5*np.sin(2*t)

    fig = go.Figure()

    fig.add_trace(go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='lines',
        line=dict(width=6,color="red")
    ))

    fig.update_layout(
        title="3D Satellite Orbit",
        scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z"
        )
    )

    return fig.to_html(full_html=False)