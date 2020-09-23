import pyaudio

from print_color import *
from print_speed import *
from record import *

from time import sleep
from datetime import datetime
import webbrowser



# Initialize a PyAudio instance
pa = pyaudio.PyAudio()

# Gets info on default input device
device_index       = pa.get_default_input_device_info()['index']
device_name        = pa.get_default_input_device_info()['name']
device_sample_rate = int(pa.get_default_input_device_info()['defaultSampleRate'])


# Global Constants
today = datetime.now()




def respond(voice_data):
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

  print_cyan("Go ahead. Ask me a question...\n")
  
  voice_data = record_user_audio(device_index, device_sample_rate)

  if voice_data is  None or voice_data == '': 
    pass
  else:

    # Slowly prints back the question user asks
    print_slow(f'{voice_data.capitalize()}?\n')
  
    # Gets answer to user's question
    answer = respond(voice_data)

    # Delays for 0.3 sec and prints answer.
    sleep(0.8)
    print_green(answer)

    # Short delay, before exiting program.
    sleep(0.5)

main()
