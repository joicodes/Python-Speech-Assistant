from print_color import print_cyan, print_green
from print_speed import print_slow
from pyaudio import PyAudio
from record import record_user_audio
from respond import respond
from speak import speak, remove_audio_file
from time import sleep

# Initialize a PyAudio instance
pa = PyAudio()

# Gets info on default input device
device_index       = pa.get_default_input_device_info()['index']
device_name        = pa.get_default_input_device_info()['name']
device_sample_rate = int(pa.get_default_input_device_info()['defaultSampleRate'])

def main():

  intro = "\nHi, I am JoiBot!"
  intro2 = "Your virtual assistant."
  intro3 = f"\nSpeak to me using your device called {device_name}."
  intro4 = "Go ahead. Ask me a question...\n"

  print(intro+"👋")
  audio_file = speak(intro)
  remove_audio_file(audio_file)

  print(intro2)
  audio_file = speak(intro2)
  remove_audio_file(audio_file)

  print(intro3)
  audio_file = speak(intro3)
  remove_audio_file(audio_file)

  print_cyan(intro4)
  audio_file = speak(intro4)
  remove_audio_file(audio_file)
  
  while True:

    voice_data = record_user_audio(device_index, device_sample_rate)

    if voice_data is None or voice_data == '': 
      pass
    else:

      # Slowly prints back the question user asks
      print_slow(f'{voice_data.capitalize()}?\n')
    
      # Gets answer to user's question
      answer = respond(voice_data)

      # Delays for 0.8 sec and prints answer and says it.
      sleep(0.8)
      print_green(answer + '\n')
      audio_file = speak(answer)

      # Removes audio file
      remove_audio_file(audio_file)

      # Exits if Goodbye
      if 'Goodbye' in answer:
        break

main()
