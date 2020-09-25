# Meet JoiBot 👋🏽
 A  Python3 speech assistant bot using the SpeechRecognition library and Google's Text-to-Speech API.
 
 ![Alt Text](https://media.giphy.com/media/HgLiAOrLElo2JG2zsJ/giphy.gif)
 
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
## Voice Commands

Here are the commands that currently exist (see `respond.txt`):

##### Meet JoiBot Commands
* What is your name? 
* Where are you from?
* Who is your creator?

##### Alarms, Timer & Clock Commands
* What time is it?
* What is today's date?
* What day of the week is it?

##### Web Query Commands
* Search for pictures of `<Search Term>`
* Search for videos of `<Search Term>`
* Where is `<Search Term>`
* Search for `<Search Term>`

##### Wildcard Commands
* Flip a coin.
* Roll the dice.
* Pick a card.

## Setup

#### Dependencies
To install the dependencies, run:
```
pip3 install -r requirements.txt
```

Alternatively, you can install individually:
```
pip3 install speechrecognition
pip3 install pyaudio
pip3 install playsound
pip3 install PyObjC
pip3 install color
```


If you experience trouble while install `pyaudio`, install [Homebrew](https://brew.sh/) and do the following:
```
brew update
brew install portaudio
brew link --overwrite portaudio
```

#### Run JoiBot
In the repo directory, run the following in your terminal:
```
python3 main.py
```
###### Note: Avoid using the terminal in your IDE, as it may not have microphone access.

