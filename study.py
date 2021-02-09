import keyboard
import time
import pyttsx3
import datetime
import threading

while True:
    try:
        should = input("Scroll? Y/N \n")
        i = int(input("Interval in seconds\n"))
        should = should.lower()
        if should == "n" and isinstance(i,int):
            sd = False
            break
        elif should == "y" and isinstance(i,int):
            sd = True
            break
        else:
            raise Exception("Try again")
    except:
        print("Try Again")
        continue        

t = datetime.datetime.now()
td = datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)

def speak(hrs, mins, secs):
    engine = pyttsx3.init()
    engine.say("Time")
    if hrs > 0:
        if hrs > 1:
            engine.say(f"{hrs} Hours")
        else:
            engine.say(f"{hrs} Hour")
    if mins > 0:
        if mins > 1:
            engine.say(f"{mins} Minutes")
        else:
            engine.say(f"{mins} Minute")
    if secs > 0:
        if secs > 1:
            engine.say(f"{secs} Seconds")
        else:
            engine.say(f"{secs} Second")
    engine.runAndWait()

while True:

    ti = datetime.datetime.now()
    tid = datetime.timedelta(hours=ti.hour, minutes=ti.minute, seconds=ti.second)
    tx = tid - td
    secs = tx.seconds % 60
    hrs = tx.seconds // 3600
    mins = (tx.seconds // 60) % 60
    # print(f"{hrs} {mins} {secs}")
    th = threading.Thread(target=speak, args=(hrs, mins, secs))
    if sd:
        keyboard.press_and_release("page down")
    th.start()
    time.sleep(i)
