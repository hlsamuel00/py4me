# DESCRIPTION:
# Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

# Use conditionals to return the proper message:

# case	return
# name equals owner	'Hello boss'
# otherwise	'Hello guest'

def greet(name, owner):
    return f"Hello {'boss' if name == owner else 'guest'}"


#==============================================================================================================

# DESCRIPTION:
# Rock Paper Scissors
# Let's play! You have to return which player won! In case of a draw return Draw!.

# Examples(Input1, Input2 --> Output):

# "scissors", "paper" --> "Player 1 won!"
# "scissors", "rock" --> "Player 2 won!"
# "paper", "paper" --> "Draw!"

def rps(p1, p2):
    choices = ['rock', 'scissors', 'paper']
    if (choices.index(p1) == (choices.index(p2) - 1) % 3):
        return 'Player 1 won!'
    elif(choices.index(p2) == (choices.index(p1) - 1) % 3):
        return 'Player 2 won!'
    else:
        return 'Draw!'

# OR

def rps(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]