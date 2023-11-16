def greeting(name):
    print(f"hello,{name}")


def user_guessing_game(secret_num,stop_num):
    user_input=' '
    while user_input != stop_num:
        user_input = input("\nGuess a number to win: ")
        if user_input == secret_num:
            print("Bingo,you guessed right and won the game")
        else:
            print(f"you entered {user_input} please try again")
