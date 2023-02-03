# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:
#     spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
#     spinWords( "This is a test") => returns "This is a test" 
#     spinWords( "This is another test" )=> returns "This is rehtona test"

def spin_words(sentence: str) -> str:
    return ' '.join(list(map(lambda word: ''.join(list(word)[::-1]) if len(word) >= 5 else word,sentence.split(' '))))

# OR

def spin_words(sentence:str) -> str:
    return ' '.join([word if len(word) > 4 else word[::-1] for word in sentence.split(' ')])

# OR

def spin_words(sentence: str) -> str:
    new_str = ''

    for idx, word in enumerate(sentence.split(' ')):
        if len(word) > 4:
            word = ''.join(list(word)[::-1])
        
        if idx < len(sentence.split(' ')) - 1:
            word += ' '
        new_str += word

    return new_str