# Shroomer's Hangman v1b
import random
# Open the word list
def hangman():
    HANGMAN_PICS = [r"""
    +---+
    |   |
        |
        |
        |
        |
    =========""", r"""
    +---+
    |   |
    O   |
        |
        |
        |
    =========""", r"""
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========""", r"""
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========""", r"""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========""", r"""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
    =========""", r"""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
    ========="""]
    fails = 0
    with open('mushroom.txt','r') as file:
        playing = True
        wordlist = file.read().splitlines()
        print(f'Word List: {wordlist}')
    # Pick a random word from a provided list
        chosenword = random.choice(wordlist)
        answer = ['_']* len(chosenword)
    # Request for a letter and loop while playing, until the game is finished
    print(HANGMAN_PICS[fails])
    while playing == True:
        print(answer)
        print(f'Fails: {fails}')
        try:
            # When given a letter check if the chosen letter is in the chosen word
            guess = input('Guess a letter, the theme is mushrooms\n')
            if guess in chosenword:
                indices = [i for i, c in enumerate(chosenword) if c == guess]
                for i in indices:
                    # Display the correct letters if any otherwise progress hangman
                    answer[i] = guess
                    print(HANGMAN_PICS[fails])
                    # See if the player has won yet
                    if ''.join(answer) == chosenword:
                        # Congrats, you won
                        print('You Win!')
                        # Ask to play again
                        repeat = input("Play again? (y/n):")
                        if repeat.upper() == 'Y':
                            # Reset the game
                            chosenword = random.choice(wordlist)
                            answer = ['_']* len(chosenword)
                            fails = 0
                            continue
                        else:
                            # End
                            return
            # If the guessed letter is NOT in the chosen word, increase fails
            # Update hangman
            elif guess not in chosenword:
                print(HANGMAN_PICS[fails])
                fails +=  1
                # See if player has lost yet
                if fails == len(HANGMAN_PICS):
                    # Better luck next time
                    print("You lose!\n")
                    # Ask to play again
                    repeat = input("Play again? (y/n):")
                    if repeat.upper() == 'Y':
                        # Reset the game
                        chosenword = random.choise(chosenword)
                        answer = ['_']* len(chosenword)
                        fails = 0
            continue
        except ValueError:
            print('Enter a character')
    
if __name__ == '__main__':
    hangman()