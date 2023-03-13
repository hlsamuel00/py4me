from random import choice
from selection import selectFromList
from settings import *

status = STATUS_DICT[selectFromList(list(STATUS_DICT.keys()), 'Do you want a completed anime or still airing?')]

print(status)

