"""
This program allows the user three tries to guess the correct answer to the question
question = "Wnat is the capital of California?". The answer is "Sacramento"
We first set max_tries = 3. The we create a loop to iterate three times. For each iteration,
We ask the user for the answer (user input). Then based on the answer the user gives, we check to see
if the user input matches the answer, If so, print "Correct". Then terminate the loop with a break
statement.

If the user could not guess the correct answer within the max_tries, the print " You have used up
you allotment of guesses." Then print " The correct anser is Sacramento."
"""
"""

main
    question = "What is the capital of California"
    answer = "Sacramento"
    ask (question, answer)

ask
    tries = 0
    loop three times
     increment tries
     ask user input()
     check to see if user input is equal to answer
      if so, print "Correct" then exit loop
if not correct
print to user "The correct answer is Sacramento."

main
"""
def main():
    question = "What is the capital of California? "
    answer = "Sacramento"
    ask(question, answer)

def ask(question, answer, max_tries=3):
    tries = 0
    ans = ""
    while tries < max_tries:
        tries = tries + 1
        ans = input(question)  # Sacramento
        if ans == answer:
            print("Correct!")
            break
    if ans != answer:
        print("You have used up your allotment of guesses")

main()


