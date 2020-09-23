from print_color import *
from print_speed import *
import pyaudio
from record import *
from respond import respond
from time import sleep


# Initialize a PyAudio instance
pa = pyaudio.PyAudio()

# Gets info on default input device
device_index       = pa.get_default_input_device_info()['index']
device_name        = pa.get_default_input_device_info()['name']
device_sample_rate = int(pa.get_default_input_device_info()['defaultSampleRate'])


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
