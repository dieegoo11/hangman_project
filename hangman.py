print("Hello, welcome to the hangman game ")
word = input('Enter in a word for someone to guess:')
print('You have 10 attempts to try and guess the word.')
turns = 0
print("_"*len(word))
place_holder = "_"*len(word)


while turns < 10:
    place_holder = list(place_holder)
    guess = input('Enter guess character:')
    if guess in word:
        print('Correct! Guess again')
        turns += 1
        for i in range(len(word)):
            if word[i] == guess:
                place_holder[i] = guess
        place_holder = ''.join(place_holder)
        print(place_holder)

    else:
        print('Wrong. Try again.')
        turns += 1
    if "_" not in place_holder:
        print('You have been declared the king of hangman!')
        break
    if turns == 10:
        print('Game over, you lost :(')
