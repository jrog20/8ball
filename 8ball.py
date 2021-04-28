"""
File: 8ball.py
Write a program to simulate a magic eight ball. The program should
let the user type a yes or no question and pick a random answer from a
set of 6 predetermined answers.
"""
import random

PROMPT = "Ask a yes or no question: "

def main():
    question = input(PROMPT)
    while question != "":
        randnum = random.randint(1, 6)
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
            print("Absolutely!")

        question = input(PROMPT)


if __name__ == '__main__':
    main()
    
