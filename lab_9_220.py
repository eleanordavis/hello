#Eleanor Davis - eleanor.davis@centre.edu - Lab 9: Word Guessing Game

#allow my player 1 to give a word to guess letters for
#make this input into a list
l_start_word = list(input('Enter the word here: '))

#create a list full of '_' (the same length as my start word) to represent my guess word
    #this guess word will end up containing a combo of letters and _'s throughout the game
l_guessed_word = list('_' * len(l_start_word))

#create a guess accumulator
i_guess = 0

#give player 2 a hint by telling how many letters are in the start word
print('The secret word has', len(l_start_word), 'letters.')

#while my guessed word does not equal my start word
while l_start_word != l_guessed_word:
    
    #allow my player 2 to input a letter they want to guess is in the word
    letter = input('Guess a letter: ')

    #for each index in the range of the length of the start word from player 1
    for i in range(len(l_start_word)):

        #if any character in the start word list equals the letter player 2 guessed:
        if  l_start_word[i] == letter:

            #make the character of the guessed word list in the same index equal that letter
            l_guessed_word[i] = letter

            #print the list of the guessed word
                #keeps player 2 updated with their progress in the game
            print(''.join(l_guessed_word))

    #increase the number of guesses by 1  
    i_guess += 1

#once the list of the guessed word equals the list of the start word
    #tell player 2 they are finished with the game
    #tell player 2 the full list of the start word
    #tell player 2 how many guesses it took them
print('Nice job, you are finished! The full word is', ''.join(l_guessed_word))
print('It took you', i_guess, 'guesses.')
    


    

