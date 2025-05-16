import numpy as np

# Generate a sine wave dataset
def generate_data(seq_length):
    x = np.linspace(0, 100, seq_length)
    y = np.sin(x)
    return y

# Example usage
if __name__ == "__main__":
    seq_length = 200
    data = generate_data(seq_length)
    print("Generated data:", data)
