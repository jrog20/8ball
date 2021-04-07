"""
File: 8ball.py
Write a program to simulate a magic eight ball. The program should
let the user type a yes or no question and pick a random answer from a
set of 6 predetermined answers.
"""
import random

PROMPT = "Ask a yes or no question: "

def main():
    # 1. Ask for y/n question
    question = input(PROMPT)

    # while the question is not an empty string
    while question != "":

        # 2. Assign to a generated a random int between 1 & 6
        randnum = random.randint(1,6)

        # 3. Print a statement associated with that randnum
        if randnum == 1:
            print("I think that it shall be!")
        if randnum == 2:
            print("Ask me again later")
        if randnum == 3:
            print("That's right")
        if randnum == 4:
            print("The answer is blowing in the wind!")
        if randnum == 5:
            print("A hard no")
        if randnum == 6:
            print("I got nothing")

        question = input(PROMPT)


if __name__ == '__main__':
    main()