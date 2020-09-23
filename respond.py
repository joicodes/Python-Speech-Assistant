from datetime import datetime
import webbrowser
import time

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
