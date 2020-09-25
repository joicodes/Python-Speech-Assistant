from datetime import datetime
from random import randint, choice
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

# For Fun
def get_coin_toss():
  flip = randint(0, 1)
  return "Head." if flip else "Tails."

def get_die_roll():
  roll = str(randint(1, 6))
  return roll

def get_card():
  suite = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
  rank = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
  return f"{choice(rank)} of {choice(suite)}."



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

  elif "flip a coin" in voice_data:
    return get_coin_toss()

  elif "roll the dice" in voice_data:
    return get_die_roll()

  elif "pick a card" in voice_data:
    return get_card()

  else:
    return "Sorry. I can't answer that question."
