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
                print(guess)

    else:
        print('Wrong. Try again.')
        turns += 1
    if turns == 10:
        print('Game over')
