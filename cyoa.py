"""Ex 06 RiddleLand."""
__author__ = "730613346"

import random

player: str = "Adventurer"  # track player's name
points: int = 5  # track adventre points

level: int = 1
PARTY_EMOJI: str = "\U0001F389"
passed: bool = True

riddles: dict[str, str] = {"What word becomes shorter when you add two letters to it?": "Short", 
                           "What is the only word in the English language that ends in \"mt\"?": "Dreamt",
                           "What is always in front of you but can't be seen?": "Future",
                           "What number is one-half of one-quarter of one-tenth of 800?": "10", 
                           "What is the value of pi to 3 decimal places?": "3.141",
                           "What is the next number in the sequence: 1, 3, 6, 10, 15, __?": "21"
                           }

history_1: str = "What country was Napoleon Bonaparte born in? "
history_2: str = "What was the name of the treaty that ended World War I and was signed on June 28, 1919? "


def main() -> None:
    """Steps of game."""
    global points
    global level
    global passed
    print("RiddleLand")
    greet()
    playing: bool = True  
    while playing:
        print(update(level, points))
        if level == 1:
            level_1()
            if passed is False:
                playing = False
                break 
            print(f"{PARTY_EMOJI} Congratulations, {player}! You passed the first level.")
            playing = choices()
        if level == 2:
            print(update(level, points))
            print("Oh-oh. Here comes the history Shphinx.")
            print("You only have one try for level 2!")
            points += level_2(points)
            playing = False
    if passed is False:
        print("It seems that you have lost all your chances.")
        print("Game Over!")
        print(update(level, points))
    else:
        print(update(level, points))  


def greet() -> None:
    """Greeting function."""
    global player
    player = input("Enter character name: ")
    print(f"Welcome, {player} to RiddleLand.")
    print("Answer the Sphinx's riddle and test your knowledge.")


def update(level: int, points: int) -> str:
    """Updates player of level and points."""
    return f" \n Your Level: {level} \n Your Adventure Points: {points} \n"


def choices() -> bool:
    """Presents player with choices."""
    global level
    global passed
    loop: bool = True
    while loop is True:
        choice: str = input("Do you want to: \n 1. Repeat level 1 \n 2. Go to level 2 \n 3. Exit game. ")
        if choice == "1":
            loop = False
            return True
        elif choice == "2":
            level += 1
            loop = False
            return True
        elif choice == "3":
            print("You have exited the game.")
            loop = False
            return False
        else: 
            print("Print choose a number between 1-2-3.")
    return True


def level_1() -> None:  # procedure function
    """Riddles for level 1."""
    global points
    global passed
    random_riddle = random.choice(list(riddles))
    print("Shphinx: \'Greetings, adventurer! Are you ready to hear my riddle?\'")
    print(f"{player}: \'Bring it on!\'")
    print(f"Shphinx: \'{random_riddle}\'")
    tries: int = 1  # Player has a total of 3 tries.
    while tries < 4:
        points -= 1  # 1 pt off for each try.
        guess: str = input("What is your answer?\n")
        if str(guess.lower()) == riddles[random_riddle].lower():
            print("Shphinx: \'That is right.\'")
            points += 5
            return
        else:
            print("Shphinx: \'Incorrect.\'")
            tries += 1
    passed = False


def level_2(pts: int) -> int:  # custom function.
    """Riddles for level 2."""  # level 2 only has one try.
    print(f"Have you studied your history, {player}?")
    global passed
    if pts < 9:
        answer_1: str = input(history_1)
        if answer_1.lower() == "france":
            print("That's correct! You earned 3 Adventure Points.")
            print(f"{PARTY_EMOJI} You won the game!")
            return 3
        else: 
            print("Wrong.")
            passed = False
            return 0
    else:
        answer_2: str = input(history_2)
        if answer_2.lower() == "the treaty of versailles" or answer_2.lower() == "treaty of versailles":
            print("You are right! You earned 5 adventure Points.")
            print(f"{PARTY_EMOJI} You won the game!")
            return 5
        else:
            print("Wrong.")
            passed = False
            return 0


if __name__ == "__main__":
    main()