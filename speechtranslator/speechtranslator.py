import speech_recognition as sr
import pyttsx3
import pyaudio
import * from googletrans
r = sr.Recognizer() #define recognizer
mic=sr.Microphone() #define microphone
print(sr.Microphone.list_microphone_names())
#this gives all the microphones connected to the device
#i want to choose the 6th one so I'll mention the index=5
mic = sr.Microphone(device_index=5)
#recognize the speech
with mic as source: 
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source) 
result = r.recognize_google(audio)
#we can even print the result using--- print(result)
#now define the translator
#language for destination can be anything
p = Translator() 
k = p.translate(result, dest='french')

#convert the translated result into text format
translated = str(k.text)
print(translated)

#define text to speech engine
engine = pyttsx3.init()

#code for terminal

#program to execute the final steps
#define the speaker language
#take id from the terminal

fr_voice_id = "com.apple.speech.synthesis.voice.Alex" engine.setProperty('voice', fr_voice_id)
#setProperty is used to define the terminal language

#final result
engine.say(translated)
engine.runAndWait()
