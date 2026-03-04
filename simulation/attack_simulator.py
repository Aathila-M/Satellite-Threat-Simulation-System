import pandas as pd
import numpy as np
import random

def generate_data(samples=5000):
    data = []

    for _ in range(samples):
        signal_strength = np.random.uniform(40, 100)
        packet_loss = np.random.uniform(0, 20)
        latency = np.random.uniform(10, 300)
        frequency_variation = np.random.uniform(0, 5)
        encryption = random.choice([0, 1])  # 0 = weak, 1 = strong
        
        # Rule-based attack labeling
        if packet_loss > 15:
            label = "DoS"
        elif frequency_variation > 3:
            label = "Jamming"
        elif encryption == 0 and latency > 200:
            label = "MITM"
        elif signal_strength < 50:
            label = "Spoofing"
        else:
            label = "Normal"

        data.append([
            signal_strength,
            packet_loss,
            latency,
            frequency_variation,
            encryption,
            label
        ])

    columns = [
        "signal_strength",
        "packet_loss",
        "latency",
        "frequency_variation",
        "encryption",
        "attack_type"
    ]

    df = pd.DataFrame(data, columns=columns)
    df.to_csv("dataset/synthetic_satellite_data.csv", index=False)
    print("Dataset Generated Successfully!")

if __name__ == "__main__":
    generate_data()