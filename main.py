import pyautogui
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import sys
import os
import cv2
import time
import requests
import json
import psutil
from datetime import date

from pyautogui import *
from playsound import playsound

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")


def time_now():
    a = datetime.datetime.now().strftime("%H")
    b = datetime.datetime.now().strftime("%M")
    t = list(b)
    if t[0] == "0":
        t.remove("0")
        Time_min = str(t)

    Time_hour = int(a) - 12

    # speak(f"the time is {Time_hour} {Time_min}")


def date_now():
    Date = date.today()
    speak(f"today's date is {Date}")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("user said : ", query)

    except Exception as e:
        print(e)
        speak("")
        return "None"
    return query


percent = ""


def battery_percentage():
    global percent
    battery = psutil.sensors_battery()
    percent = battery.percent
    speak(f"my energy level is {percent} percentage")


def there_exists(terms, query):
    for term in terms:
        if term in query:
            return True

    pass


if __name__ == "__main__":
    while True:
        print("Activating APSIT... ")
        speak("activating APSIT")
        speak("Hey sir   ,  I   am your personal assistant")
        wishme()
        date_now()
        # time_now()
        battery_percentage()
        speak("how can i help you")
        while True:
            if percent <= 20:
                speak("my energy level is getting too low,   its just")
                speak(percent)
                speak("percentage only")
                speak("i am gonna die ,  please connect charger")
                speak("or else i'll shutdown")

            query = takecommand().lower()

            if 'whatsup dude' in query:
                speak("nothing buddy, whatsup")

            elif 'feeling sleepy' in query:
                speak("no buddy, i like to spend time with you")

            elif 'are you active' in query:
                speak("yeah buddy, i am listening")

            elif 'how are you' in query:
                speak("i am good buddy,hoe may i help you")

            elif 'tell us about yourself' in query:
                speak("i am your virtual friend, you can ask me any help at any time , i will do for you buddy")

            elif 'weather forecast' in query:
                speak("enter your name of the city buddy")
                city = input("Enter your city name : ")
                speak("wait a moment buddy, i am checking ")
                speak("according to today's weather")
                webbrowser.open(f"{city} weather")

            elif "what's the time now" in query:
                time_now()

            elif "what's the date today" in query:
                date_now()

            elif 'open wikipedia' in query:
                speak("what do you want from wikipedia buddy")
                search = takecommand()
                speak("searching in wikipedia")
                results = wikipedia.summary(search, sentences=2)
                speak("according to wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                speak("opening youtube")
                webbrowser.open("youtube.com")

            elif 'open gmail' in query:
                webbrowser.open("gmail.com")
                speak("gmail is opened")

            elif 'open home' in query:
                webbrowser.open("http://moodle.apsit.org.in/moodle/")

            elif 'open python' in query:
                webbrowser.open("http://moodle.apsit.org.in/moodle/course/view.php?id=2158")

            elif 'open lab' in query:
                webbrowser.open("http://moodle.apsit.org.in/moodle/course/index.php?categoryid=385")

            elif 'open portal' in query:
                webbrowser.open("https://admission.apsit.org.in/")

            elif 'open google' in query:
                speak("opening google")
                speak("what do you want to search in google")
                search = takecommand().lower()
                webbrowser.open("https://google.com", new=1)
                time.sleep(5)
                typewrite(search)
                press("enter")

            elif 'play some videos' in query:
                speak("playing video ,  have fun buddy")

            elif 'play song' in query:
                speak("Playing song, Enjoy the song buddy")
                playsound('music.mp3')

            elif 'send message' in query:
                pywhatkit.sendwhatmsg("+917977436563","this is testing protocol",15,31)

            elif 'tell me how much energy do you have' in query:
                battery_percentage()

            elif 'open camera' in query:
                speak("opening camera")
                cam = cv2.VideoCapture(0)
                while True:
                    img = cam.read()[1]
                    cv2.imshow('camera', img)
                    k = cv2.waitKey(10)
                    if k == 27:
                        break
                cam.release()
                cv2.destroyAllWindows
                exit(cv2)

            elif 'take screenshot' in query:
                speak("Taking Screenshoot")
                screenshot = pyautogui.screenshot()
                screenshot.save("screen.png")
                speak('Captured screenshot is saved in Screenshots folder')

            elif 'write a note' in query:
                speak("What should i write, sir")
                note1 = input("Enter what you want to add :" )
                file = open('APSIT.txt', 'w')
                file.write('')
                file.write(note1)

            elif 'location' in query:
                query = query.replace("where is", "")
                location = query
                speak("User asked to locate")
                place = input("Enter your place to locate : ")
                webbrowser.open("https://www.google.nl//maps/place/" + place + "")

            elif 'see u later buddy' in query:
                speak(" bye   buddy ")
                speak("if    you    need   anything   you   can   call   me   at any time ")
                speak(" i    will    be   there   for    you")
                break
