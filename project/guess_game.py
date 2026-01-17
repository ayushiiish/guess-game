import random as rnd
while True:   
    secret_number = rnd.randint(0, 100)
    attempts = 3
    i = 0
    print("\n I have chosen a number between 0 and 100.")
    while i < attempts:
        user_input = input("Guess the number: ")
        if not user_input.isdigit():
            print("Wrong input! Please write in integer.")
            continue
        num=int(user_input)
        if num==secret_number:
            print("You won!")
            break
        else:
            print("Wrong guess!")
            i += 1

    if i == attempts:
        print(f"The secret number was {secret_number}.")
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing ")
        break
        
