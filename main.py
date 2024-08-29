#create a random word and check character if they are in the word
import os
import random
import hangman_art
# we can also write as
#from hangman_art import logo
#then we can use simple logo we dont have to use hangman_art.logo
import hangman_words

print(hangman_art.logo)
word_list = hangman_words.list
randomword = random.choice(word_list)
word_length = len(randomword)
display= []
lives = 6
gamewon = False


for _ in range(word_length):
    display += "_"

while not gamewon :

    guesscharacter = input("Guess a Letter: ").lower()


    os.system("cleara")

    print(randomword)
    if guesscharacter in display:
        print(f"You Guess {guesscharacter}, You have already guess this letter")
    else:
        for position in range(word_length):
            letter = randomword[position]
            if letter == guesscharacter:
                display[position] = letter
                print(f"You Guess {guesscharacter} , it is in the word ")


    if guesscharacter not in randomword:
        print(f"You Guess {guesscharacter},that is not in the word")
        lives -= 1
        if lives == 0:
            gamewon = True
            print("Game Over,You Lost")


    if '_' not in display:
        gamewon = True
        print ("Game Over,You Won")


    print(display)
    print(hangman_art.stages[lives])
print(f"The Hidden Word is {randomword}")

# this is manoush code 