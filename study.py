import keyboard
import time
import pyttsx3
import datetime
import threading

while True:
    try:
        shouldScroll = input("Scroll? Y/N \n")
        interval = int(input("Interval in seconds\n"))
        shouldScroll = shouldScroll.lower()
        if shouldScroll == "n" and isinstance(interval,int):
            sd = False
            break
        elif shouldScroll == "y" and isinstance(interval,int):
            sd = True
            break
        else:
            raise Exception("Try again")
    except:
        print("Try Again")
        continue        

startTime = datetime.datetime.now()
startTimeDelta = datetime.timedelta(hours=startTime.hour, minutes=startTime.minute, seconds=startTime.second)

def speak(hrs, mins, secs):
    engine = pyttsx3.init()
    engine.say(" ")
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

    presentTime = datetime.datetime.now()
    presentTimeDelta = datetime.timedelta(hours=presentTime.hour, minutes=presentTime.minute, seconds=presentTime.second)
    elapsed = presentTimeDelta - startTimeDelta
    secs = elapsed.seconds % 60
    hrs = elapsed.seconds // 3600
    mins = (elapsed.seconds // 60) % 60
    # print(f"{hrs} {mins} {secs}")
    speechthread = threading.Thread(target=speak, args=(hrs, mins, secs))
    if sd:
        keyboard.press_and_release("page down")
    speechthread.start()
    time.sleep(interval)
