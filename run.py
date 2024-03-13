#This is my python program

#Emoji shows thumbs up
import sys
from emoji import emojize

print(emojize(":thumbs_up:"))

#Displays a cat picture ^.^
from cat_picture.cat import pic
pic()

#Get a random joke
import pyjokes
print(pyjokes.get_joke())