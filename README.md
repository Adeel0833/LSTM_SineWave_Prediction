# LSTM Sine Wave Prediction

This project implements a simple LSTM model to predict the next value in a sine wave sequence. The model is trained using a generated sine wave dataset and deployed using Gradio for easy interaction.

## Project Structure
```
/LSTM_SineWave_Prediction
├── app.py          # Gradio application
├── model.py        # Model training and saving
├── dataset.py      # Sine wave data generation
├── requirements.txt # Project dependencies
└── README.md       # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd LSTM_SineWave_Prediction
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model:
   ```bash
   python model.py
   ```

4. Run the Gradio application:
   ```bash
   python app.py
   ```

## Usage
- Enter a sequence length in the Gradio interface.
- The model will predict the next value in the sine wave sequence based on the trained LSTM model.

## Additional Information
- The model is saved as `lstm_model.h5` after training.
- The data generation and model training logic are modularized in `dataset.py` and `model.py`.
