from random import choice
from selection import selectFromList
from settings import *

genre = choice(MOOD_DICT[selectFromList(MOOD_DICT, 'What mood are we going for?')])

print(genre)

