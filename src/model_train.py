# Human milk nutrition prediction after reduction
#
# Corresponding Author: Sasha Chernenkoff, sasha.chernenkoff@ucalgary.ca
#
# model_train - script for training the neural network
#
# Author: Sasha Chernenkoff
# Date: 3 March, 2024


import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Read in training data
data = pd.read_csv('../data/training_data.csv', header=None)

# Split data into features (X) and targets (y)
# X: fat, carbs, protein, calories, % reduction
# y: fat, carbs, protein, calories
X = data.iloc[:, :5].values  # Feature matrix
y = data.iloc[:, 5:].values  # Target matrix

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Build the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(y_train.shape[1])
])

model.compile(optimizer='adam',
              loss='mean_squared_error',
              metrics=['mean_squared_error'])

# Train the model
fit = model.fit(X_train, y_train, epochs=500, validation_split=0.2, verbose=1)

# Evaluate the model
test_loss, test_mse = model.evaluate(X_test, y_test, verbose=1)
print(f"Test MSE: {test_mse}")

# Plot the training curve
pd.DataFrame(fit.history).plot()
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

# Save the model
model.save('../bin/model.h5')

# Save the scaler
scaler_filename = "../bin/scaler.save"
joblib.dump(scaler, scaler_filename)