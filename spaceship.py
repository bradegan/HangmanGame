'''
    CS5001
    Fall 2018
    HW5
    Brad Egan
'''

from random import choice
import turtle

# Set dictionary and scores filenames.
DICT_FILE = 'wordlist.txt'
SCORES_FILE = 'scores.txt'


def initiate_rocket_game():
    ''' Function: initiate_rocket_game
        Parameters: none
        Returns: nothing
        Does: calls run_game function and calculates score.
              Prompts user to play again or not.
              Writes based on 2 methods depending on whether
              or not high score. Uses write_highscore function
              if highscore, otherwise uses append_score function.
    '''
    
    score = 0
    play_again = True
    
   # Runs game while play_again is true.
    while play_again == True:
        score += run_game()
        print("Score is:", score, "\n")
        play_again = play_or_not(prompt_play_again())

    # Reads highscore and if highscore uses write_highscore function.
    if score >= float(read_highscore(SCORES_FILE)):
        name = input("Please enter your name \n")
        write_highscore(name, score, SCORES_FILE)

    # Appends score to end of score file.
    else:
        name = input("Please enter your name \n")
        append_score(name, score, SCORES_FILE)

def read_wordlist(filename):
    ''' Function: read_wordlist
        Parameters: filename, a string for .txt file
        Returns: wordlist, a list
        Does: Opens filename using read parameter. Reads into a list
              using readlines. Close file, and returns list.
    '''
    
    try:
        infile = open(filename, 'r')
        wordlist = infile.readlines()
        infile.close()
        return wordlist
    except OSError:
        print("Error reading file")
    

def choose_random_word(filename):
    ''' Function: choose_random_word
        Parameters: filename, a string for .txt file
        Returns: word, a string
        Does: Calls read_wordlist function to make a list of words.
            Then chooses random element from list using choice function.
            Strips, linebreaks, spaces, switches word to lowercase and
            returns random word.    
    '''

    wordlist = read_wordlist(filename)    
    random_word = choice(wordlist)
    random_word = random_word.strip('\n')
    random_word = random_word.strip()
    random_word = random_word.lower()
    return random_word

def run_game():
    ''' Function: run_game
        Parameters: none
        Returns: score, an integer
        Does: Main game function. Chooses random word using
              choose_random_word function.
              Then draws spaces the number of letters in the random word.
              Keeps track of wrong guesses, wrong letters, guessed letters,
              and score of user. Tracks letter location to draw out correct
              letters.
              Removes letters from random word until length is zero.
              Returns score of user's game.
        
    '''

    wrong_guesses = 0
    original_random_word = choose_random_word(DICT_FILE)
    random_word = original_random_word
    draw_spaces(len(original_random_word))
    score = 0
    guessed_letters = []
    wrong_letters = []

    while wrong_guesses < 5:
        guess = prompt_input_char()

        # Checks correct guess, draws letter and removes from random word.
        if guess in random_word and guess not in guessed_letters:
            letter_location = find_letter_location(guess, original_random_word)
            guessed_letters.append(guess)
            draw_letters(letter_location, guess)
            random_word = remove_letter(guess, random_word)

            # Breaks and user wins if len of random word is reduced to zero.
            if len (random_word) == 0:
                print("You win, random word is", original_random_word)
                score += 1
                break

        # Check if already guessed letter
        elif guess in guessed_letters:
            print("You already guessed", guess, "please guess again.")

        # Wrong guess drawn out
        else:
            wrong_guesses += 1
            wrong_letters.append(guess)
            draw_wrong_guesses(wrong_guesses, guess)
    print("The word was", original_random_word)
    return score

def draw_wrong_guesses(wrong_guesses, guess):
    ''' Function: draw_wrong_guesses
        Parameters: wrong_guesses, an int for # of wrong guesses
                    guess, a string for a letter guessed
        Returns: nothing
        Does: Draws appropriate flame / rocket / body according to
              wrong_guesses number. Draws wrong letter using
              draw_wrong_letter function.
    '''

    
    print("Wrong guesses are", wrong_guesses)

    if wrong_guesses == 1:
        draw_body()
    elif wrong_guesses == 2:
        right_rocket()
    elif wrong_guesses == 3:
        left_rocket()
    elif wrong_guesses == 4:
        left_flame()
    elif wrong_guesses == 5:
        right_flame()
        print("You lose, sorry!!")
        
    draw_wrong_letter(wrong_guesses, guess)


def draw_spaces(length):
    ''' Function: draw_spaces
        Parameters: length, an int for # of spaces
        Returns: nothing
        Does: Draws length number of blank spaces
    '''

    turtle.speed(0)
    turtle.penup()
    turtle.goto (300, -250)
    turtle.setheading(180)
    for i in range (length):
        turtle.pendown()
        turtle.forward(25)
        turtle.penup()
        turtle.forward (15)
        turtle.hideturtle()

def draw_letter(position, letter):
    ''' Function: draw_letter
        Parameters: position, an int, an negative index
                    letter, a string, letter to be drawn 
        Returns: nothing
        Does: Draws letter at a given position on right side
              of screen
    '''

    turtle.speed(0)
    turtle.penup()
    turtle.goto (300, -250)
    turtle.setheading(180)
    for i in range(-position):
         turtle.penup()
         turtle.forward(40)

    turtle.backward(22)
    turtle.right(180)

    turtle.write(letter, font=("Arial", 18, "bold"))
    turtle.forward(40)
    turtle.hideturtle()

def draw_letters (position_list, letter):
    ''' Function: draw_letters
        Parameters: position_list, a list of negative indicies
                    letter, a str
        Returns: nothing
        Does: Draws given letter at different index positions
              on right side of screen
    '''

    for position in position_list:
        draw_letter(position, letter)

def draw_wrong_letter(position, letter):
    ''' Function: draw_wrong_letter
        Parameters: position, an int, index
                    letter, a str
        Returns: nothing
        Does: Draws wrong letters on left side of screen
    '''

    turtle.speed(0)
    turtle.penup()
    turtle.goto (-320, -250)
    turtle.setheading(0)
    for i in range(position):
        turtle.forward(20) 
    turtle.write(letter, font=("Arial", 15, "bold"))
    turtle.resizemode
    turtle.hideturtle()
    

def prompt_play_again():
    ''' Function: prompt_play_again
        Parameters: none
        Returns: again, a str, "Y"/"N"
        Does: Prompts user for a "Y" or a "N"
    '''

    again = input("Play again? Enter Y/N \n")
    again = again.upper()
    while again != "Y" and again != "N":
        again = input("Play again? Enter Y/N \n")
        again = again.upper()
    return again

def play_or_not(again):
    ''' Function: play_or_not
        Parameters: again, a string
        Returns: boolean - True / False
        Does: returns True if "Y" and resets board otherwise returns False
    '''

    
    if again == "Y":
        turtle.reset()
        turtle.hideturtle()
        return True
    else:
        return False

def prompt_input_char():
    ''' Function: prompt_input_char
        Parameters: none
        Returns: letter, a str of length 1
        Does: Prompts user to enter a letter of length one
              Lowercases letter and reprompts user for letter
              if input entered is not length one.
    '''

    letter = input("Guess a letter \n")
    letter = letter.lower()
    if len (letter) != 1:
       return prompt_input_char()
    else:
        return letter

def remove_letter(letter, word):
    ''' Function: remove_letter
        Parameters: letter, a str
                    word, a str
        Returns: word
        Does: Removes all instances of a given letter in a word.
    '''

    word = list(word)
    while letter in word:
        word.remove(letter)
    word = ''.join(word)
    return word



def find_letter_location(letter, word):
    ''' Function: find_letter_location
        Parameters: letter, a str
                    word, a str
        Returns: position, a list
        Does: returns negative index list of positions of given letter
              in word
    '''

    position = []
    word = list(word)
    for i in range(len(word)):
        if letter == word[i]:
            position.append(-(len(word)-i))
    return position


def read_highscore(filename):
    ''' Function: read_highscore
        Parameters: filename, a str
        Returns: high_score, an int
        Does: Reads highscore from highscore file.
    '''

    score_list = read_scorelist(filename)
    if len(score_list) == 0:
        return (float("-inf"))
    else:    
        high_score = score_list[0]
        high_score = high_score.split(" ")
        high_score = high_score[-1].strip("\n")
        return int(high_score)

def read_scorelist(filename):
    ''' Function: read_scorelist
        Parameters: filename, a str
        Returns: list
        Does: Reads score_list file into a list
              If file does not exist returns empty list.
    '''

    try:
        infile = open(filename, 'r')
        score_list = infile.readlines()
        infile.close()
        return score_list
    except OSError:
        return []
    

def write_highscore(name, high_score, filename):
    ''' Function: write_highscore
        Parameters: name, a str
                    high_score, an int
                    filename, a str
        Returns: nothing
        Does: Writes name and highscore to top of given filename
    '''

    score_list = read_scorelist(filename)
    outfile = open(filename, 'w')
    try:
        score_list = [name + " " + str(high_score) + "\n"] + score_list
        outfile.writelines(score_list)

    except TypeError:
        score_list = [name + " " + str(high_score) + "\n"]
        outfile.writelines(score_list)
    except OSError:
        print ("Error writing file")
    outfile.close()


def append_score(name, score, filename):
    ''' Function: append_score
        Parameters: name, a str
                    score, an int
                    filename, a str
        Returns: nothing
        Does: Appends score to bottom of filename .txt file.
    '''

    try:
        outfile = open(filename, 'a')
        outfile.write(name + ' ' + str(score) + "\n")
        outfile.close()
    except OSError:
        print ("Error writing file")

def draw_body():
    ''' Function: draw_body
        Parameters: none
        Returns: nothing
        Does: Draws rocket body
    '''

    turtle.penup()
    turtle.goto(0,175)
    turtle.pendown()
    turtle.goto(-50,100)
    turtle.goto(-50,-100)
    turtle.goto(50,-100)
    turtle.goto(50,100)
    turtle.goto(0,175)
    turtle.hideturtle()

def left_rocket():
    ''' Function: left_rocket
        Parameters: none
        Returns: nothing
        Does: Draws left rocket
    '''

    turtle.penup()
    turtle.goto(-70,-50)
    turtle.pendown()
    turtle.goto(-40,-130)
    turtle.goto(-100,-130)
    turtle.goto(-70,-50)
    turtle.hideturtle()


def left_flame():
    ''' Function: left_flame
        Parameters: none
        Returns: nothing
        Does: Draws left flame
    '''

    
    turtle.penup()
    turtle.goto(-100,-130)
    turtle.pendown()
    turtle.goto(-90,-150)
    turtle.goto(-80,-130)
    turtle.goto(-70,-160)
    turtle.goto(-60,-130)
    turtle.goto(-50,-150)
    turtle.goto(-40,-130)
    turtle.hideturtle()


def right_rocket():
    ''' Function: right_rocket
        Parameters: none
        Returns: nothing
        Does: Draws right rocket
    '''

    turtle.penup()
    turtle.goto(70,-50)
    turtle.pendown()
    turtle.goto(40,-130)
    turtle.goto(100,-130)
    turtle.goto(70,-50)
    turtle.hideturtle()

def right_flame():
    ''' Function: right_flame
        Parameters: none
        Returns: nothing
        Does: Draws right flame
    '''

    turtle.penup()
    turtle.goto(100,-130)
    turtle.pendown()
    turtle.goto(90,-150)
    turtle.goto(80,-130)
    turtle.goto(70,-160)
    turtle.goto(60,-130)
    turtle.goto(50,-150)
    turtle.goto(40,-130)
    turtle.hideturtle()

