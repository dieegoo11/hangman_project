print("Hello, welcome to the hangman game ")
word = input('Enter in a word for someone to guess:')
print('You have 10 attempts to try and guess the word.')
print("_"*len(word))
turns = 0
place_holder = "_"*len(word)

while turns < 10:
    guess = input('Enter guess character:')
    if guess in word:
        print('Correct! Guess again')
        turns += 1
    else:
        print('Wrong. Try again.')
        turns += 1
