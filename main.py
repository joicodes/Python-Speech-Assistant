import speech_recognition as sr
import pyaudio
from print_color import *
from print_speed import *
from time import sleep
from datetime import datetime
import webbrowser

# Initialize a recognizer
recognizer = sr.Recognizer()

# Initialize a PyAudio instance
pa = pyaudio.PyAudio()

# Gets info on default input device
device_index       = pa.get_default_input_device_info()['index']
device_name        = pa.get_default_input_device_info()['name']
device_sample_rate = int(pa.get_default_input_device_info()['defaultSampleRate'])


# Global Constants
today = datetime.now()


def record_user_audio():
  # To use default microphone as audio source
  with sr.Microphone(device_index=device_index, sample_rate=device_sample_rate) as source:

    # # Calibrates the energy threshold for ambient noise levels for 1 second.
    # recognizer.adjust_for_ambient_noise(source, duration=1)
 
    voice_data = ''
    try:
        # Records a single phrase from source. Times out after 30 seconds.
        audio = recognizer.listen(source, timeout=10)
        # Recognize speech using Google Speech Recognition API.
        voice_data = recognizer.recognize_google(audio)
    except sr.WaitTimeoutError:
      print("Hello? Are you there?")
    except sr.UnknownValueError:                                    
      print("Sorry, I didn't get that.")
    except sr.RequestError:
      print("😓 Well, this is awkward. My speech services is not working. Try again later.")
    return voice_data


def respond(voice_data):
  sleep(.5)
  if 'your name' in voice_data:
    return 'My name is JoiBot 🤖'

  elif 'time' in voice_data:
    now = datetime.now()
    return now.strftime("%I:%M %p")

  elif "date" in voice_data:
    return today.strftime("%A, %B %-d, %Y")

  elif "day of the week" in voice_data:
    return today.strftime('%A')

  else:
    return "Sorry. I can't answer that question."



def main():

  print("\nHi, I am JoiBot! 👋")
  print("You're virtual assistant.")

  print(f"\nSpeak to me using your {device_name}.")
  print_cyan("Go ahead. Ask me a question...\n")
  
  voice_data = record_user_audio()

  if voice_data != '' or voice_data != None: 
    print_slow(f'{voice_data.capitalize()}?\n')
    bot_response = respond(voice_data)
    sleep(0.3)
    print_green(bot_response)
    sleep(0.5)

main()
