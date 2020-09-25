from datetime import datetime
from random import randint, choice
import webbrowser
import time

today = datetime.now()


# Commands for JoiBot 

# About JoiBot
def get_name():
  return 'My name is JoiBot.'

def get_hometown():
  return 'I am from the Big Apple.'

def get_creator():
  return 'I was created by Joi Anderson.'

# Alarms, Timer & Clock Commands
def get_time():
  now = datetime.now()
  return now.strftime("%I:%M %p")

def get_date():
  return today.strftime("%A, %B %-d, %Y")

def get_weekday():
  return today.strftime('%A') 

# TO DO: Web Search Commands

def search_google():
  pass

def search_google_img():
  pass
def search_youtube():
  pass

def search_wikipedia():
  pass

def search_google_maps():
  pass

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

  voice_data = voice_data.lower()

  if 'bye' in voice_data:
    return 'Nice talking to you! Goodbye.'
  
  elif 'your name' in voice_data:
    return get_name()

  elif 'where are you from' in voice_data:
    return get_hometown()

  elif 'created' in voice_data or 'creator' in voice_data:
    return get_creator()

  elif 'time' in voice_data:
    return get_time()

  elif "date" in voice_data:
    return get_date()

  elif "day of the week" in voice_data:
    return get_weekday()

  elif "search" in voice_data:
    if "video" in voice_data:
      return search_youtube()
    elif "photo" in voice_data:
      return search_google_img()
    elif "wikipedia" in voice_data:
      return search_wikipedia()
    else:
      return search_google()

  elif "where is" in voice_data:
    return search_google_maps()

  elif "flip a coin" in voice_data:
    return get_coin_toss()

  elif "roll the dice" in voice_data:
    return get_die_roll()

  elif "pick a card" in voice_data:
    return get_card()

  else:
    return "Sorry. I can't answer that question."
