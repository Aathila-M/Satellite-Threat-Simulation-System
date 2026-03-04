import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

df = pd.read_csv("dataset/synthetic_satellite_data.csv")

X = df.drop("attack_type", axis=1)

model = IsolationForest(contamination=0.1)

model.fit(X)

pickle.dump(model, open("models/anomaly_model.pkl","wb"))

print("Anomaly Detection Model Created")