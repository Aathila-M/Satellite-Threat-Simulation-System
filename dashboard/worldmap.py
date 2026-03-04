import pandas as pd
import plotly.express as px

def attack_map():

    data = {
        "country": ["USA","Russia","China","India"],
        "lat":[37.77,55.75,39.90,28.61],
        "lon":[-122.41,37.61,116.40,77.20],
        "attack":["DoS","Jamming","MITM","Spoofing"]
    }

    df = pd.DataFrame(data)

    fig = px.scatter_geo(
        df,
        lat="lat",
        lon="lon",
        color="attack",
        title="Global Cyber Attacks"
    )

    return fig.to_html(full_html=False)