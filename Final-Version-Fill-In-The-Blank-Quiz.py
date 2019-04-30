guessCounter = 5

guessIndex = 0

outOfLives = 0

blankList = ["BLANK1", "BLANK2", "BLANK3", "BLANK4"]

promptList = ['What do you think fills "BLANK1"? ',
              'What do you think fills "BLANK2"? ',
              'What do you think fills "BLANK3"? ',
              'What do you think fills "BLANK4"? ']

easyMode ='''

[EASY MODE]The current problem reads: Twenty BLANK1 from now you will be more BLANK2 by the things that you BLANK3 do than by the ones you BLANK4 do.

'''

easyList = ["years", "dissapointed", "didn't", "did"]

mediumMode ='''

[MED. MODE]The current problem reads: I'm a BLANK1 today because I had a BLANK2 who BLANK3 in me and I didn't have the BLANK4 to let him down.

'''

mediumList = ["success", "friend", "believed", "heart"]

hardMode = '''

[HARD MODE]The current problem reads: It is BLANK1 to escape the BLANK2 that people commonly use false standards of measurement - that they seek power, success and BLANK3 for themselves and admire them in others, and that they underestimate what is of true BLANK4 in life.


'''

hardList = ["impossible", "impression", "wealth", "value"]

def show_intro():
    """This function will show the user tips on how to get started with the quiz and select difficulty"""
    print("""
    Welcome to my Quiz! Please select your difficulty from below:

    Easy Peezy Lemon Squeezy - Type: Easy

    You Can Probably Handle This... Maybe - Type: Medium

    Almost Impossible - Type: Hard

    **You will get 5 guesses per blank regardless of difficulty
    """)

def difficulty_selector():
    """
    This function will prompt the user to select a difficulty out of the available choices.

    Input:
        The user selects between "easy", "medium" or "hard."
    Behavior:
        Once user has selected the difficulty it will assign the difficulty and answers based
        on that choice.
    Return:
        This function will return the difficulty and answer variables for question_prompter().
    """
    answer_choices = ["easy","medium", "hard"]
    new_answer = raw_input("Please feel free to type your answer here: ").lower()
    while new_answer not in answer_choices:
        print("That's not a valid answer! Please select from Easy, Medium or Hard.")
        new_answer = raw_input("Please feel free to type your answer here: ").lower()
    if new_answer == "easy":
        difficulty = easyMode
        answers = easyList
    elif new_answer == "medium":
        difficulty = mediumMode
        answers = mediumList
    elif new_answer == "hard":
        difficulty = hardMode
        answers = hardList
    return question_prompter(difficulty, answers, guessIndex)

def question_prompter(difficulty, answers, guessIndex):
    """
    This function will prompt the user to guess for the current BLANK.

    Input:
        The user will input their guess for the corresponding BLANK.
    Behavior:
        This will ask the user for a guess based on the guessIndex to correspond with correct prompt
    Return:
        This function will return the new_answer through the answer_checker to check users response.
    """
    global guessCounter
    print(difficulty)
    while guessCounter > outOfLives:
        new_answer = raw_input(promptList[guessIndex]).lower()
        return answer_checker(new_answer, answers, difficulty)

def answer_checker(new_answer, answers, difficulty):
    """
    This function will check the users response against the correct answers.

    Input:
        This will receive the users newest response as well as the current answer list and difficulty.
    Behavior:
        Loop through each correct answer and check if the newest response matches the current answer.
        If there is a match, move the guessIndex to the next prompt
            check game_status in case game is over
            reset the guess counter
        If there is no match, remove a guess
            check game_status in case game is over
            alert user of incorrect response and remaining guesses, if any.
    Return:
        This function will return the question_prompter with either the same guessIndex (response was wrong) or new guessIndex (response was correct).
    """
    global guessIndex
    global guessCounter
    for answer in answers:
        if new_answer in answers:
            difficulty = answer_filler(answers, difficulty)
            print("That's correct!!\n")
            guessIndex += 1
            if guessIndex == len(answers):
                return end_game(1, difficulty)
            guessCounter = 5
            return question_prompter(difficulty, answers, guessIndex)
    else:
        guessCounter -= 1
        if guessCounter == outOfLives:
            end_game(0, difficulty)
        else:
            print("Uh oh, that's incorrect! You currently have {} guesses left!\n").format(guessCounter)
            return question_prompter(difficulty, answers, guessIndex)

def answer_filler(answers, difficulty):
    """
    This function will add the correct answer to the problem if the user guesses correctly.

    Input:
        This will receive the correct answer and current difficulty problem.
    Behavior:
        Take difficulty and break it into a list of strings
        Loop through each word in difficulty
        If the word matches the current BLANK, replace it with current word from correct answer list and add to new_difficulty
        remaining words can be added to new_difficulty with no change
        combine new list into one string
    Return:
        This function will return the updated difficulty the fills correctly answered blanks
    """
    global guessIndex
    new_difficulty = []
    difficulty = difficulty.split()
    for word in difficulty:
        if word == blankList[guessIndex]:
            word = answers[guessIndex]
            new_difficulty.append(word)
        else:
            new_difficulty.append(word)
    new_difficulty = " ".join(new_difficulty)
    return new_difficulty

def end_game(game_status, difficulty):
    """
    This function will check if the game win or lose conditions have been met and end game accordingly.

    Input:
        This will receive the current game_status and current difficulty.
    Behavior:
        If answer_checker() sees that guessCounter equals outOfLives it will send a game status of 0 is sent to this function.
        A game_status of 0 will end the game and print the corresponding message.
        If answer_checker sees that guessIndex equals the length of the answer list a game status of 1 is sent to this function.
        a game_status of 1 will end the game and print the finished problem with corresponding message
    Return:
        This function will end the game.
    """
    if game_status == 0:
        print("""
        **Game Over!**
        Uh oh! Looks like the last guess was incorrect and you're out of guesses now.
        Better luck next time!""")
    else:
        print('''
        Completed Quiz:
        {}

        You won!!! Nice Job completing that quiz!!!''').format(difficulty[38:])

def play_game():
    """This game will begin the game by showing the intro function and running the difficulty selector function."""
    show_intro()
    difficulty_selector()

play_game()
