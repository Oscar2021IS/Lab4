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


