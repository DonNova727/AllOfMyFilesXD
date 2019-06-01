import random
from urlilib.request import urlopen
import sys

WORLD_URL = "https://learncodethehardway.org/words.text"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "Class %%%(object):\n\tdef__init__(self, ***)":
        "class %%% has-a __init__ that takes self and ***params.",
    "class %%%(object):\n\tdef ***(self, @@@":
        "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the function, call it with params self, @@@.",
    "***.*** ='***'":
        "From *** get the *** attribute and set it to '***'."
}