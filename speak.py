from gtts import gTTS
import os
import random
from playsound import playsound


def create_audio_file_name():
    num = random.randint(1, 10000)
    audio_file_name = f'joibot-audio-{num}.mp3'
    return audio_file_name

def remove_audio_file(audio_file):
    os.remove(audio_file)

def speak(answer):
    # Speech synthesis using Google Text to Speech
    tts = gTTS(text=answer, lang='en')

    # Generates a audiofile name and saves tts
    audio_file = create_audio_file_name()
    tts.save(audio_file)

    # Plays the audio file
    playsound(audio_file)

    # Returns the name of the file
    return audio_file
