import gradio as gr
import numpy as np
import tensorflow as tf
from dataset import generate_data

# Load the trained model
model = tf.keras.models.load_model('lstm_model.h5')

# Define the prediction function
def predict_sine_wave(seq_length):
    # Generate the sine wave data
    data = generate_data(seq_length)
    window_size = 10
    test_input = data[-window_size:].reshape((1, window_size, 1))
    prediction = model.predict(test_input)
    return prediction[0][0]

# Gradio Interface
iface = gr.Interface(fn=predict_sine_wave, inputs="number", outputs="text", 
                     title="LSTM Sine Wave Prediction",
                     description="Predict the next value in a sine wave using LSTM")

# Launch the Gradio app
if __name__ == "__main__":
    iface.launch()
