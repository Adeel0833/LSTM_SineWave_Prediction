import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Generate a sine wave dataset
def generate_data(seq_length):
    x = np.linspace(0, 100, seq_length)
    y = np.sin(x)
    return y

# Create dataset
seq_length = 200
window_size = 10

data = generate_data(seq_length)

X = []
Y = []
for i in range(len(data) - window_size):
    X.append(data[i:i + window_size])
    Y.append(data[i + window_size])

X = np.array(X)
Y = np.array(Y)
X = X.reshape((X.shape[0], X.shape[1], 1))

# Define LSTM model
model = Sequential()
model.add(LSTM(50, activation='relu', input_shape=(window_size, 1)))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# Train the model
model.fit(X, Y, epochs=100, verbose=1)

# Save the trained model
model.save('lstm_model.h5')
