"""
==========================================================
Project : Number Guessing Game
==========================================================

Description:
The user thinks of a number between 1 and 100.

The computer guesses the number by asking:

- higher
- lower
- correct

The program uses Binary Search Logic,
so it finds the answer in very few attempts.

Concepts Used
-------------
- Variables
- Functions
- if-elif-else
- while loop
- Integer
- String
- User Input

Author : Ayushi Kasundra
==========================================================
"""
def welcome():
    
    print("=" * 50)
    print("      NUMBER GUESSING GAME")
    print("=" * 50)

    print("\nThink of a number between 1 and 100.")
    print("I will try to guess your number.")
    print("\nReply using only:")
    print("higher")
    print("lower")
    print("correct")

    input("\nPress Enter when you are ready...")
def get_response(question):
    
    while True:

        answer = input(question).strip().lower()

        if answer in ["higher", "lower", "correct"]:
            return answer

        print("\nInvalid Input!")
        print("Please enter only:")
        print("higher")
        print("lower")
        print("correct")

def guess_number():

    low = 1
    high = 100

    attempts = 0

    while low <= high:

        guess = (low + high) // 2

        attempts += 1

        print("\n" + "-" * 40)
        print(f"Attempt : {attempts}")
        print(f"My Guess : {guess}")
        print("-" * 40)

        answer = get_response(
            "Is your number Higher, Lower or Correct? : "
        )

        # User's number is greater
        if answer == "higher":

            low = guess + 1

        # User's number is smaller
        elif answer == "lower":

            high = guess - 1

        # Computer guessed correctly
        elif answer == "correct":

            print("\n🎉 Hurray!")
            print(f"I guessed your number: {guess}")
            print(f"Total Attempts : {attempts}")

            return

    print("\nSomething went wrong!")
    print("Please answer the questions correctly.")
def main():
    
    welcome()

    guess_number()

    print("\n" + "=" * 50)
    print("Thank you for playing!")
    print("Have a Nice Day!")
    
    print("=" * 50)

if __name__ == "__main__":
    main()