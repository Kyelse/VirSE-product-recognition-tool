import speech_recognition as sr
from helpers import textToSpeech as tts

def speechToText():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Do you want take photo (yes/no): ")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            print("You said: {}".format(text))
        except:
            tts.textToSpeech("Sorry, could not recognize your voice")