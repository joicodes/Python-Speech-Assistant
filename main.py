import speech_recognition as sr
import pyaudio

# Initialize a recognizer
recognizer = sr.Recognizer()

# Initialize a PyAudio instance
pa = pyaudio.PyAudio()

# Gets info on default input device
device_index       = pa.get_default_input_device_info()['index']
device_name        = pa.get_default_input_device_info()['name']
device_sample_rate = int(pa.get_default_input_device_info()['defaultSampleRate'])

# To use default microphone as audio source
with sr.Microphone(device_index=device_index, sample_rate=device_sample_rate) as source:

    # Print statement to prompt user to say something. 
    print("\nHi, I am JoiBot, you're virtual assistant. 👋")
    print(f"You can speak to me using your device called {device_name}.")
    print("\nDon't believe me? Try it!")

    while True:

        # Calibrates the energy threshold for ambient noise levels for 1 second.
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Say something...")

        # Listens for user response for up to 10 seconds.
        audio = recognizer.listen(source, timeout=30)

        try:

            # Recognize speech using Google Speech Recognition.
            voice_data = recognizer.recognize_google(audio)

            # Prompts user to confirm if speech recognition was correct.
            print(f'\nDid you say "{voice_data}"? 🤔') 
            print(f'If correct, say "Yes". If not, say "No"')

            confirm_audio = recognizer.listen(source, timeout=30)
            response = recognizer.recognize_google(confirm_audio)

            # If "yes", print confirmation greeting and exit.
            if response == "yes":
                print("\nNice. I heard you loud and clear! 😄")
                break
            # If "no", print apology and loops again to try again.
            elif response == "no":
                print("\nSorry that I did not hear you. 😓\n Let's try again! ")
            else:
                print("\nThat was not a valid response. Goodbye!👋")
                break

        except LookupError:                                    
            print("Could not understand audio")

