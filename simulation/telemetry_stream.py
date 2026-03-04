import random
import time
import json

def generate_telemetry():

    telemetry = {
        "signal_strength": random.randint(40,100),
        "packet_loss": random.uniform(0,20),
        "latency": random.randint(10,300),
        "frequency_variation": random.uniform(0,5),
        "temperature": random.randint(-20,60),
        "power_level": random.randint(50,100)
    }

    return telemetry


if __name__ == "__main__":

    while True:

        data = generate_telemetry()

        print(json.dumps(data))

        time.sleep(2)