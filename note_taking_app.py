import speech_recognition as sr
import gtts
from playsound import playsound
import os
from datetime import datetime

r = sr.Recognizer()

def get_audio():
    with sr.Microphone() as source:
        print("say something")
        audio = r.listen(source)
    return audio

def audio_to_text(audio):
    text = ""
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("audio not recognized")
    except sr.RequestError:
        print("Results from API failed")
    return text

def play_sound(text):
    try:
        tts = gtts.gTTS(text)
        tempfile = "./temp.mp3"
        tts.save(tempfile)
        playsound(tempfile)
        os.remove(tempfile)
    except AssertionError:
        print("Failed to play sound")



