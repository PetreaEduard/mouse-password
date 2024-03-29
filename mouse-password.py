import time
import random
import threading
from pynput import keyboard, mouse

# Initialize lists to store timestamps
key_timestamps = []
mouse_timestamps = []

# Define a function to log key presses
def on_key_press(key):
    key_timestamps.append(time.time())

# Define a function to log mouse movements
def on_mouse_move(x, y):
    mouse_timestamps.append(time.time())

# Create keyboard and mouse listeners
keyboard_listener = keyboard.Listener(on_press=on_key_press)
mouse_listener = mouse.Listener(on_move=on_mouse_move)

# Start the listeners
keyboard_listener.start()
mouse_listener.start()

# Run the listeners in the background
keyboard_thread = threading.Thread(target=keyboard_listener.join)
mouse_thread = threading.Thread(target=mouse_listener.join)
keyboard_thread.start()
mouse_thread.start()

# Wait for some time (e.g., 10 seconds)
print('MOVE THE MOUSE!')
time.sleep(10)

# Stop the listeners
keyboard_listener.stop()
mouse_listener.stop()

file_path = "entropy.txt"
# Calculate time intervals between key presses and mouse movements
key_intervals = [key_timestamps[i+1] - key_timestamps[i] for i in range(len(key_timestamps)-1)]
mouse_intervals = [mouse_timestamps[i+1] - mouse_timestamps[i] for i in range(len(mouse_timestamps)-1)]

with open('entropy.txt','w') as f:
    for mouse_interval in mouse_intervals:
        f.write(f"{mouse_interval}\n")

# Read data from the external entropy file (replace with the actual path)
def read_entropy_file(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    return data

# Generate random numbers using the external entropy data
def generate_random_numbers(entropy_data, num_samples):
    random.seed(entropy_data)  # Seed the random number generator
    random_numbers = [random.random() for _ in range(num_samples)]
    return random_numbers

# Example usage
entropy_file_path = "entropy.txt"  # Replace with the actual path to your entropy file
external_entropy_data = read_entropy_file(entropy_file_path)
num_samples = 16 # Number of random numbers to generate

# Assuming you have a list of randomly generated numbers
# Replace this with your actual list of numbers
random_numbers = [random.randint(1, 127) for _ in range(len(generate_random_numbers(external_entropy_data, num_samples)))]
word = ""

# Print the resulting list of numbers
for i in random_numbers:
    word = word + chr(i)

print('Your new password is ' + word)
