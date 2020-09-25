import speech_recognition as sr
from print_color import print_cyan, print_red

# Initialize a recognizer
recognizer = sr.Recognizer()

def record_user_audio(device_index, sample_rate):
  with sr.Microphone(device_index=device_index, sample_rate=sample_rate) as source:

    attempts = 0
    
    while attempts <= 2: 
      voice_data = None

      try:
          # Records a single phrase from source.
          audio = recognizer.listen(source, timeout=5)
          
          # Recognize speech using Google Speech Recognition API.
          voice_data = recognizer.recognize_google(audio)

      except (sr.WaitTimeoutError, sr.UnknownValueError):

        if attempts < 2:
          print("Sorry, I didn't get that. 😅")
          print_cyan("Ask me again...\n")
          attempts += 1
          continue

        else:
          print("I still can't hear you. 😓")
          print_red("Try again later.\n")
          return None 

      except sr.RequestError:
        print("😓 Well, this is awkward. My speech services is not working.")
        print_red("Try again later.")
        break

      return voice_data
