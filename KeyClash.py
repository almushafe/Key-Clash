import keyboard
import time 

a = input("Enter your Name first : ")
b = input("Enter your Name second  : ")

f1 = 0
s1 = 0

while True:

    if keyboard.is_pressed('w') or keyboard.is_pressed('up') :
        f1 += 1  # Increase score by 1
        s1 -= 1
        print(f"{a} vs {b} : --------- [ {f1} ]---- vs ----[ {s1} ]---------")
        time.sleep(0.1)  # Small delay to avoid multiple detections when key is held down

    if keyboard.is_pressed('s') or keyboard.is_pressed('down') :
        f1 -= 1  # Decrease score by 1
        s1 += 1
        print(f"{a} vs {b} : ----------[ {f1} ]---- vs ----[ {s1} ]---------")
        time.sleep(0.1)  # Small delay to avoid multiple detections when key is held down

    # Check if the 'esc' key is pressed to exit the program
    if keyboard.is_pressed('esc'):
        print(f"{a} vs {b} : ---------- [ {f1 } ]---- vs ---- [ {s1} ]---------")  # Print final score
        if f1 < s1 :
            print(f"won {b}")
            print(f"defeat {a}")
        elif f1 > s1 :
            print(f"won : {a}")
            print(f"defeat : {b}")
        elif f1 == s1:
            print("Draw : {a} vs {b}")
        break  # Exit the loop
