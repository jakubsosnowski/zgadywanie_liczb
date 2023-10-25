from random import randint

comp_choose = randint(1, 100)

while True:
    try:
        user_choose = int(input("Guess the number: "))
    except ValueError:
        print("It's not a number!")
        continue
    if user_choose > 100 or user_choose < 0:
        print("Please enter value with range 0-100")
        # I added this waring because user doesn't know range of number
    elif user_choose < comp_choose:
        print("Too small!")
    elif user_choose > comp_choose:
        print("Too big")
    else:
        print("You win!")
        break
