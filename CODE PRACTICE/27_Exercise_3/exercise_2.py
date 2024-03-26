# Create a program capable of displaying questions to the user like KBC. Use List data type to store the questions and their correct answers. Display the final amount the person is taking home after playing the game.
import random

winingAmt = 0
questionAns = [
    ["What is the capital of india.", "New Delhi"],
    ["Republic day celebrate in India.", "26-Jan"],
    ["Independence day celebrate in India.", "15-Aug"],
]

print("\tWelcome to KBC")
question = random.choice(questionAns)
print("Question:", question[0])
ans = input("Your Answer: ")
if ans == question[1]:
    print("Correct Answer :)")
    print("Your Wining Amt is: ", winingAmt + 100)
else:
    print("Wrong Answer :(")
    print("Your Wining Amt is: ", winingAmt - 100)

while True:
    question = random.choice(questionAns)
    print("\nQuestion:", question[0])
    ans = input("Your Answer: ")
    if ans == question[1]:
        print("Correct Answer :)")
        print("Your Wining Amt is: ", winingAmt + 100)
    else:
        print("Wrong Answer :(")
        print("Your Wining Amt is: ", winingAmt - 100)

    wantsExit = input("You Want to Exit From Program (Y/N): ")
    if wantsExit == "Y":
        exit(0)
