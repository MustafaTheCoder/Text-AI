import pyttsx3 
import datetime
import wikipedia 
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

while True:
    user_inp = input("> ")

    if user_inp == "open code".lower():
        speak("Opening Code...")
        print("Opening Code...")
        code_path = "Path"
        os.startfile(code_path)

    elif user_inp == "open google".lower():
        speak("Opening Google...")
        print("Opening Google...")
        google_path = "Path"
        os.startfile(google_path)

    elif user_inp == "time".lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"The time is {strTime}")
        print(f"Time: {strTime}")
        
    else:
        break    
