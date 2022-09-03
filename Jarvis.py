#packages for project
from winreg import QueryValueEx
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<3:
        speak("What's up in the Midnight!")
    elif hour>=3 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("Hello I am Jarvis. Do you need an assist?")

def takeCommand():
    #It takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5 #seconds of non-speaking audio before a complete phrase
        r.energy_threshold = 100 #minimum audio energy to consider for recording
        r.dynamic_energy_ratio = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('piclu26072003@gmail.com','xxxxx')
    server.sendmail('anushkachowdhury2019.com',to,content)
    server.close()


if __name__ == '__main__':
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
    # logic for executing tasks based on query
        if 'wikipedia' in query:
           speak('Searching Wikipedia...')
           query = query.replace("wikipedia","")
           results = wikipedia.summary(query, sentences=2)
           speak("According to Wikipedia")
           print(results)
           speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open whatsapp' in query:
            wpPath = "C:\\Users\\HP\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(wpPath)
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
        elif 'open spotify' in query:
            webbrowser.open('spotify.com')
        elif 'play music' in query:
            music_dir = 'C:\\Users\\HP\\Music\\Playlists'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Aniket, the time is {strTime}")
        elif 'atom' in query:
            atomPath = "C:\\Users\\HP\\AppData\\Local\\atom\\atom.exe"
            os.startfile(atomPath)
        elif 'send mail to Pakhi' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "anushkachowdhury2019@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry,Aniket, I am unable to send the email")
        elif 'what is your name' in query:
            speak("My name is Jarvis, Sir!")
        
        ##elif 'play music' in query:
            ##mp3_updated = 'C:\\Users\\HP\\OneDrive\\Desktop\\Hackathon\\mp3_updated.py'
            ##os.startfile(mp3_updated)
