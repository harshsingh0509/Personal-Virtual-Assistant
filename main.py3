import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import os

def speck(text):
    
    engine = pyttsx3.init()
    
    # setting the speed
    engine.setProperty('rate',150)
    
    # setting the voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    
    engine.say(text)
    engine.runAndWait()
    
def takeVoiceCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(query)
        return query
    except Exception as e:
        print(e)
        print("sorry say again.")
        

if __name__== "__main__":
    speck("hello harsh! iam your virtual assistant nimbus . Let me know how can i help you?")
    while True:
        command = takeVoiceCommand().lower()
        if command == "who are you":
            speck("I am nimbus")
            
        elif "assistant" in command:
            speck("my assistant is echo")
            
        elif "play hua main on youtube" in command:
            webbrowser.open("https://youtu.be/5V04DETPF0o?si=fHTTDi2FIkgTJuNr")
            
        elif "play lover on youtube" in command:
            webbrowser.open("https://youtu.be/-BjZmE2gtdo?si=jkUIdP-x33WoQ2wz")
            
        elif "play let her go by passenger on spotify" in command:
            webbrowser.open("https://open.spotify.com/track/2pUpNOgJBIBCcjyQZQ00qU?si=795c894462e04191")
            
        elif "open google" in command:
            webbrowser.open("https://google.com/")
            
        elif "open wikipedia" in command:
            speck("searching in wikipedia.......")
            command = command.replace("wikipedia","")
            result = wikipedia.summary(command,sentence = 2)
            speck("according to wikipedia")
            print(result)
            speck(result)

