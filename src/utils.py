import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


# Prediction function (using TensorFlow model)
def predict_nutrition(features):
    # Load the model
    model = tf.keras.models.load_model('../bin/model.h5')

    # Load the scaler
    scaler_filename = "../bin/scaler.save"
    scaler = joblib.load(scaler_filename)

    features_scaled = scaler.transform(features)
    predicted_nutrition = model.predict(features_scaled)
    return predicted_nutrition[0]