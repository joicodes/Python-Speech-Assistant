from datetime import datetime
from random import randint, choice
import webbrowser
import time
from urllib.parse import quote

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

def search_google(query):
  encoded_query = quote(query)
  url = f"https://www.google.com/search?q={encoded_query}"
  webbrowser.get().open(url)
  return "This is what I found on Google."

def search_google_img(query):
  url = f"https://www.google.com/search?q={quote(query)}&tbm=isch"
  webbrowser.get().open(url)
  return "Here are some images I found on the web."

def search_youtube(query):
  url = f"https://www.youtube.com/results?search_query={quote(query)}"
  webbrowser.get().open(url)
  return "Here are videos I found on YouTube."

def search_google_maps(query):
  url = f"http://maps.google.com/?q={quote(query)}"
  webbrowser.get().open(url)
  return "Here is what I found on Google Maps."

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
      query = voice_data.split("of",1)[1]
      return search_youtube(query)
    elif "photo" in voice_data:
      query = voice_data.split("of",1)[1]
      return search_google_img(query)
    else:
      query = voice_data.split("for",1)[1]
      return search_google(query)

  elif "where is" in voice_data:
    query = voice_data.split("where is",1)[1]
    return search_google_maps(query)

  elif "flip a coin" in voice_data:
    return get_coin_toss()

  elif "roll the dice" in voice_data:
    return get_die_roll()

  elif "pick a card" in voice_data:
    return get_card()

  else:
    return "Sorry. I can't answer that question."

