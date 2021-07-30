import random
import string
continueGame = "Y"

#list of words
words = ['table', 'chair', 'bed', 'blanket', 'pillow']
word = random.choice(words)  # randomly chooses something from the list

def hangman():
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set()  # what the user has guessed
    wins = 0
    lose = 0
    lives = 6 #chance for user to miss the words
    continueGame = len(words) #for continue next game
    att = 0



    # getting user input
    while len(word_letters) > 0 and lives > 0:
        
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print("You have yo guess the word. The clue is about things in your room") #tell the clue
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        #checking the guess of words
        user_letter = input('Guess a letter: ').lower() 
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters: #mengindikasi bahwa huruf tersebut sudah digunakan
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')
        
        elif user_letter in used_letters: #tell user that the world has used before
            print('\nYou have already used that letter. Guess another letter.')

        else: #if user input incorrect character (it's mean not a letter)
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        lose += 1
        print('You died, sorry. The word was', word)
        print('SCORE WIN : ', wins, 'Lost: ', lose)
    else:
        wins += 1
        print('YAY! You guessed the word', word, '!!')
        print('SCORE:  WIN : ',wins, 'Lost: ',lose)
    
    att += 1
    
    #for continue or finish the game
    if att < 3:
      continueGame = input("Do you want to play again? Y to continue, any other key to quit")
      if continueGame.upper() == 'Y': #continue
        hangman()
            
      else:
        print("Thank You for playing. See you next time!") #finish

if __name__ == '__main__': #running the program
    hangman()