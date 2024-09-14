import os
import speech_recognition as sr
import pyttsx3
import requests
from gtts import *
import pygame
# import musicLibrary
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init() 



def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 


# def processCommand(c):
#     try:
#         speach = c.lower()
#         print(speach)
#     except Exception as e:
#         speak("Sorry Sir Currently I cannot do that")

def play():
    print("The Fuctiuon is Called")
    def st():
        speak("Listening....")
    
        print("Starting Recorgnizer")
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=17, phrase_time_limit=1)
                print("Jarvis Active...")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                # print(command)
                # processCommand(command)
                return command
        except Exception as e:
            print("Don't Hear anything".format(e))
    return st()