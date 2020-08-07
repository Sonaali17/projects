#run this in terminal
import pyttsx3
import pyaudio
import * from googletrans
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print("Voice:") 
    print(" - ID: %s" % voice.id) 
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages) 
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
