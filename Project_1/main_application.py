import datetime
import wikipedia
import webbrowser
import os
from speech_recognition import recognize_speech
from text_to_speech import speak


def greet_user():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your voice assistant. How can I help you today?")

def fetch_wikipedia(query):
    speak('Searching Wikipedia...')
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)

def open_app(app_name):
    if "notepad" in app_name:
        os.system("notepad")
    elif "browser" in app_name:
        webbrowser.open("https://google.com")
    else:
        speak("Sorry, I can't open that application.")

def tell_time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {strTime}")

# Example usage
greet_user()
command = recognize_speech()
if 'wikipedia' in command:
    command = command.replace("wikipedia", "")
    fetch_wikipedia(command)
elif 'time' in command:
    tell_time()
elif 'open' in command:
    open_app(command)
