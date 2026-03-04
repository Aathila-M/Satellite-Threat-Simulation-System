from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model

app = Flask(__name__)

# ================= LOAD MODELS =================

model = pickle.load(open("models/threat_model.pkl", "rb"))
anomaly_model = pickle.load(open("models/anomaly_model.pkl", "rb"))
deep_model = load_model("models/deep_attack_model.h5")


# ================= DATA FUNCTIONS =================

def get_attack_stats():
    df = pd.read_csv("dataset/synthetic_satellite_data.csv")
    counts = df["attack_type"].value_counts().to_dict()
    return counts


# ================= ROUTES =================

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/network")
def network():
    return render_template("network.html")


@app.route("/simulation")
def simulation():
    return render_template("simulation.html")


# ================= ANALYTICS =================

from dashboard.plots import attack_pie

@app.route("/analytics")
def analytics():
    plot = attack_pie()
    return render_template("analytics.html", plot=plot)


# ================= 3D ORBIT =================

from dashboard.orbit import satellite_orbit

@app.route("/orbit")
def orbit():
    plot = satellite_orbit()
    return render_template("orbit.html", plot=plot)


# ================= WORLD MAP =================

from dashboard.worldmap import attack_map

@app.route("/worldmap")
def worldmap():
    plot = attack_map()
    return render_template("worldmap.html", plot=plot)


# ================= SIGNAL HEATMAP =================

from dashboard.heatmap import signal_heatmap

@app.route("/heatmap")
def heatmap():
    plot = signal_heatmap()
    return render_template("heatmap.html", plot=plot)


# ================= CYBER ATTACK MAP =================

@app.route("/cybermap")
def cybermap():
    return render_template("cybermap.html")


# ================= PREDICTION =================

@app.route("/predict", methods=["GET", "POST"])
def predict():

    # If user refreshes or navigates back
    if request.method == "GET":
        return render_template("index.html")

    features = [
        float(request.form["signal_strength"]),
        float(request.form["packet_loss"]),
        float(request.form["latency"]),
        float(request.form["frequency_variation"]),
        int(request.form["encryption"])
    ]

    # RandomForest prediction
    prediction = model.predict([features])[0]

    # IsolationForest anomaly detection
    anomaly = anomaly_model.predict([features])[0]

    if anomaly == -1:
        anomaly_result = "⚠ Anomaly Attack Detected"
    else:
        anomaly_result = "Normal Traffic"

    # Deep Learning prediction
    deep_pred = deep_model.predict(np.array([features]))
    deep_pred_value = int(np.argmax(deep_pred))

    stats = get_attack_stats()

    return render_template(
        "dashboard.html",
        result=prediction,
        anomaly=anomaly_result,
        deep_result=deep_pred_value,
        stats=stats
    )


# ================= DASHBOARD =================

@app.route("/dashboard")
def dashboard():
    stats = get_attack_stats()
    return render_template("dashboard.html", stats=stats)


# ================= TELEMETRY GRAPH =================

from dashboard.telemetry import telemetry_graph

@app.route("/telemetry")
def telemetry():
    plot = telemetry_graph()
    return render_template("telemetry.html", plot=plot)


# ================= 3D EARTH ORBIT =================

from dashboard.earth_orbit import earth_orbit

@app.route("/earth")
def earth():
    plot = earth_orbit()
    return render_template("earth.html", plot=plot)


# ================= RUN SERVER =================

if __name__ == "__main__":
    app.run(debug=True)