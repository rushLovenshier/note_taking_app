import speech_recognition as sr
import gtts
from playsound import playsound
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv('.env')

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

CMD = os.environ.get('ACTIVATION_COMMAND')

while True:
    a = get_audio()
    command = audio_to_text()

    if CMD in command.lower():
        print("activated")
        play_sound("what can I do for you?")

        note = get_audio()
        note = audio_to_text(note)

        if(note):
            play_sound(note)

            now = datetime.now().astimezone().isoformat()
            