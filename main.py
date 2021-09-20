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

def wikipedia(arg):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

while True:
    user_inp = input("> ")

    if user_inp == "open code".lower():
        speak("Opening Code...")
        print("Opening Code...")
        code_path = "C://Users//MUHAMMAD DANISH//AppData//Local//Programs//Microsoft VS Code//Code.exe"
        os.startfile(code_path)

    elif user_inp == "open google".lower():
        speak("Opening Google...")
        print("Opening Google...")
        google_path = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"
        os.startfile(google_path)

    elif user_inp == "open youtube".lower():
        speak("Opening Youtube...")
        print("Opening Youtube...")
        #implementation

    elif user_inp == "the time":
        strTime = datetime.datetime.now().strftime("%H:%M:%S")    
        speak(f"Sir, the time is {strTime}")

        
    else:
        break    



