from gtts import gTTS # google text to speech
import speech_recognition as sr

import os

'''voice =""
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            if text =="stop":
                break
            text = r.recognize_google(audio)
            voice = voice + str(text)
        except:
            print("Say Something.....")
hr = gTTS(text=voice,Lang='em',slow=False)
hr.save("myvoice.wav")'''


mytext = input()
language ='en'

myobj = gTTS(text=mytext,lang=language,slow=False)
myobj.save("myvoice1.mp3")

os.system("mpg32 1 myvoice1.mp3") # playing the converted file
