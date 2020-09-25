from datetime import datetime
import webbrowser
import time

# Global Constants
today = datetime.now()

# Commands for JoiBot 
def get_time():
  now = datetime.now()
  return now.strftime("%I:%M %p")

def get_date():
  return today.strftime("%A, %B %-d, %Y")

def get_weekday():
  return today.strftime('%A') 



# Returns a response based on voice data
def respond(voice_data):
  if 'bye' in voice_data:
    return 'Nice talking to you! Goodbye.'
  
  elif 'your name' in voice_data:
    return 'My name is JoiBot.'

  elif 'time' in voice_data:
    return get_time()

  elif "date" in voice_data:
    return get_date()

  elif "day of the week" in voice_data:
    return get_weekday()

  else:
    return "Sorry. I can't answer that question."
