"""IPND Stage 2 Fill-In-The-Blanks Quiz. 
This project is a MapleStory Trivia Fill-in-the-Blanks game.
There are 3 difficulty levels that can be chosen. 
After choosing the difficulty level, the player then chooses 
how many maximum attempts for each blank.
The game will present a user with a paragraph containing several blanks.
The player will then be asked to fill in each blank appropriately to 
complete the paragraph. 
The player wins if all blanks are filled correctly."""

easy_level = """When 'MapleStory' first launched, the very first playable class 
was the __1__ class. Today, the __1__ class remains one of several 
different character classes. When an __1__ character is first created, 
he or she starts on __2__ Island, the weakest area in the game. The weakest 
monster, green __3__, is prevalent on __2__ Island. At level 10, the player 
can choose a 1st job advancement - Magician, __4__, Archer, Thief or Pirate."""
easy_answers = ['Explorer', 'Maple', 'snail', 'Warrior']

medium_level = """In 'MapleStory', you need to be level __1__ to get the 2nd job 
advancement. Once you hit level __1__, you need to speak to the 
__2__ that gave you your 1st job advancement. Archer class players 
should speak to __3__ Pierce who resides in Henesys. There are 2 
paths to choose at this point - Hunter or __4__."""
medium_answers = ['30', 'NPC', 'Athena', 'Crossbowman']

hard_level = """'MapleStory' encourages players not only to __1__ but also involve 
themselves in __2__ Quests. For players between levels 61 - 75, the 
__3__ Park PQ is a tantalizing option. __3__ Park is available from 
any town with the Safari Jeep NPC in it. Players can exchange ticket 
pieces here and get the __4__ Safari Tickets to enter the MPQ area 
which scales to the player's level. Between levels 141 - 180, players 
should aim to complete the __5__ Invasion PQ. Unlike __3__ Park, the 
__5__ Invasion PQ can only be done __6__ times a day."""
hard_answers = ['grind', 'Party', 'Monster', 'Golden', 'Dimension', '5']

def choose_difficulty_level():
    """Prompts player for difficulty level. Repeats until player chooses valid level.
    Function returns a string: either 'easy', 'medium', or 'hard'"""
    prompt = "\nPlease enter difficulty level. You may choose 'easy', 'medium' or 'hard': "
    options = ['easy', 'medium', 'hard']
    chosen_difficulty = raw_input(prompt).lower()
    while chosen_difficulty not in options:
        print "\nYour selection is invalid. Please try again."
        chosen_difficulty = raw_input(prompt).lower()
    print "\nYou've chosen " + chosen_difficulty
    return chosen_difficulty


def fix_max_attempts():
    """Prompts player for maixum attempts per question. 
    Repeats until number chosen is a positive integer.
    Function returns player-selected maximum number of attempts."""
    prompt = "\nPlease choose your desired maximum number of attempts " 
    prompt += "\nper question before GAME OVER: "
    chosen_max_attempts = raw_input(prompt)
    while int(chosen_max_attempts) <= 0:
        print "\nPositive integers only please."
        chosen_max_attempts = raw_input(prompt)
    print "\nYou will get " + str(int(chosen_max_attempts)) + " guesses per problem."
    return chosen_max_attempts


def generate_para(diff_level):
    """Function takes a difficulty level (easy, medium, or hard) as the input.
    Returns corrsponding paragraph and answer list."""
    if diff_level == 'easy':
        return (easy_level, easy_answers)
    if diff_level == 'medium':
        return (medium_level, medium_answers)
    if diff_level == 'hard':
        return (hard_level, hard_answers)


def blank_filler(base_para, blank_num, answer, chosen_max_attempts):
    """Takes the base paragraph (str), current blank (int), answer (str) and player-defined max attempts.  
    Returns the partially answered paragraph (or None if the player
    takes too many guesses) and the number of the next blank."""
    attempts_left = int(chosen_max_attempts)
    to_replace = '__' + str(blank_num) + '__'
    prompt = '\nThe current paragraph reads as such:\n\n{}\n\n'
    prompt += 'What should be substituted in for {}? '
    prompt = prompt.format(base_para, to_replace)
    user_guess = raw_input(prompt).lower()
    while user_guess != answer.lower() and attempts_left > 1:
        attempts_left -= 1
        print prompt + '\n\nWrong!\nTry Again.'
        user_guess = raw_input(prompt).lower()
    if attempts_left > 1:
        print '\nCorrect!\n'
        return (base_para.replace(to_replace, answer), blank_num + 1)
    else:
        return (None, blank_num + 1)


def play_game():
    """Gameplay execution function.
    Returns try_another_level() to allow player to try again."""
    diff_level = choose_difficulty_level()
    base_para, answers = generate_para(diff_level)
    max_guesses = fix_max_attempts()
    current_blank = 1
    while current_blank <= len(answers):
        base_para, current_blank = blank_filler(base_para, current_blank, answers[current_blank - 1], max_guesses)
        if base_para is None:
            print "GAME OVER"
            return try_another_level()

    print base_para + '\n\nCongratulations!\nYou\'ve won!\n'
    return try_another_level()


def try_another_level():
    """Function executes after GAME OVER or victory. 
    Allows player to try another level if 'y' selected.
    Choosing 'n' shuts the program."""
    prompt = 'Return to selection screen and try another level?\n'
    prompt += 'Enter Y/N: '
    player_choice_options = ['y', 'n']
    player_choice = raw_input(prompt).lower()
    while player_choice not in player_choice_options:
        print "\nYour selection is invalid. Please try again."
        player_choice = raw_input(prompt).lower()
    if player_choice == 'y':
        print play_game()
    if player_choice == 'n':
        print "\nSee you again."
        return False

print play_game()

 