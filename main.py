import speech_recognition as sr
from gtts import gTTS
import os
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import cv2
from requests import get
import webbrowser
import feedparser
from GoogleNews import GoogleNews
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.say("hello boss")
engine.say("i am  you jarvis")
engine.say("say wakeup to activate")
engine.runAndWait()


def talk(text):
    engine.say(text)
    print(text)
    engine.runAndWait()





def jarvis():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1
        r.adjust_for_ambient_noise(source, duration=1)
        audio=r.listen(source)
    try:
        print("plese wait boss")
        command=r.recognize_google(audio,language='en-in')
        print(f"you just said: {command}\n")
        
    except Exception as e:
        print(e)
        talk("please tell me again")
        command="none"
    return command    


def wakeUpCommands():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("jarvis is sleeping...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio, language='en-in')
        print(f"user said: {command}\n")
    except Exception as e:
        command = "none"
    return command

if name == "main":
    while True:
        command = wakeUpCommands().lower()
        if "wake up" in command:
            talk("yes Boss what can I do for you")
            while True:
                command=jarvis().lower()
                if "play" in command:
                    song = command.replace('play', '')
                    talk("playing" + song)
                    print(song)
                    pywhatkit.playonyt(song)
                elif "time" in command:
                    time = datetime.datetime.now().strftime("%H:%M")
                    print(time)
                    talk("the time is " + time)
                elif "who is" in command:
                    person = command.replace("who is", '')
                    info = wikipedia.summary(person, 1)
                    talk(info)
                elif "date" in command:
                    talk("Sorry, I have a headache")
                elif "open camera" in command:
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(50)
                        if k == 27:
                            break
                    cap.release()
                    cv2.destroyAllWindows()
                elif "are you single" in command:
                    talk("yes I am just like you")
                elif "dumb" in command:
                    talk("no but i think you are")    
                elif "joke" in command:
                    joke = pyjokes.get_joke()
                    talk(joke)
                elif "search" in command:
                    website_name = command.replace("search", "")
                    pywhatkit.search(website_name)
                elif "news" in command:
                    command = command.replace("news", "")
                    google_news_url = "https://news.google.com/rss"
                    news_feed = feedparser.parse(google_news_url)
                    for entry in news_feed.entries:
                        print("Title:", entry.title)
                        talk(entry.title)
                        
                elif "ip address" in command:
                    ip = get('https://api.ipify.org').text
                    talk(f"your IP address is {ip}")    

while True:
    jarvis()
