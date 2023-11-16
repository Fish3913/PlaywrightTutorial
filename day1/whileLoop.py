# a=0
# while a < 5:
#     print(f"hello,{a}")
#     a += 1  #same as a=a+1
#
#     for a in range(5):
#         print()
user_input = ' '
while user_input != '-1':
    user_input = input(" Guess a number to win: ")
    if user_input == '77':
        print("Bingo,you guessed right and won the game")
    else:
        print(f"you entered {user_input} please try again")