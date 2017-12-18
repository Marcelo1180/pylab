#!/usr/bin/env python3
# sudo apt-get install portaudio19-dev
# pip install PyAudio

import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile("audio.wav") as source:
    audio = r.record(source)

try:
    s = r.recognize_google(audio)
    print("Text: "+s)
except Exception as e:
    print("Exception: "+str(e))

