import random

def number(num):
    user_input = int(input("Guess the number (between 1 and 10): "))
    if num == user_input:
        print("Hurray!! 🎉 You won the game!")
        opinion = str(input("Do you want to play again? (yes or no): "))
        if opinion == "yes":
            num = random.randint(1, 10)
            number(num)
        else:
            print("Hope you enjoyed the game! 😊")
    elif num > user_input + 2:
        print("Too small number ❌")
        number(num)
    elif num > user_input:
        print("Small number, you are very close! 😉")
        number(num)
    elif num < user_input - 2:
        print("Too big number ❌")
        number(num)
    elif num < user_input:
        print("Big number, you are very close! 😉")
        number(num)

print("✨ Guess the Number Game 🎮")
num = random.randint(1, 10)
number(num)
