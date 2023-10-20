
import keyboard


while True:
    if keyboard.is_pressed("1"):
        while True:
            if keyboard.is_pressed("0"):
                print("stopped")
                break
            print("moving")