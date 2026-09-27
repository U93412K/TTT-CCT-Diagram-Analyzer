import numpy as np

def generate_cooling_curve(initial_temperature, cooling_rate, duration=100, points=1000):
    """Generate a simple linear cooling curve."""
    time = np.linspace(0, duration, points)
    temperature = np.maximum(initial_temperature - cooling_rate * time, 0)
    return time, temperature
