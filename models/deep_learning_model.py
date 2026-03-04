import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("dataset/synthetic_satellite_data.csv")

X = df.drop("attack_type",axis=1)
y = df["attack_type"]

encoder = LabelEncoder()
y = encoder.fit_transform(y)

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(32,activation="relu"),
    tf.keras.layers.Dense(16,activation="relu"),
    tf.keras.layers.Dense(5,activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.fit(X_train,y_train,epochs=20)

model.save("models/deep_attack_model.h5")

print("Deep Learning Model Created")