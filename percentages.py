import time
from random import seed
from random import random

from threading import Timer

# seed random number generator
seed(10)
start = time.time()
gameTime = 120
numRight = 0
numTot = 0
maxDenom = 50
ERROR_MARGIN = 1


def runKill():
    for _ in range(20):
        print(".")
    print(
        "{} correct and {} incorrect for an accuracy of {}".format(
            numRight, numTot, (numRight * 100 / numTot)
        )
    )
    for _ in range(10):
        print(".")


# t = Timer(gameTime, print, ['Sorry, times up'])
t = Timer(gameTime, runKill)


def makeNum(maxNum):
    # Create a random number between 1 and maxNum-1
    # the '-1' means the denominator never equals the numerator for trivial x/x
    temp = float(int(random() * (maxNum - 1)))
    if temp == 0:
        return 1
    else:
        return temp


userAns = 0.0
error = 999
t.start()
while True:
    # create question
    denominator = makeNum(maxDenom)
    numerator = makeNum(denominator)

    # create answer
    ans = 100 * numerator / denominator

    while error > ERROR_MARGIN:
        # user input answer
        userAns = input(
            "what is {} as a percentage of {}\n".format(numerator, denominator)
        )
        try:
            userAns = float(userAns)
        except Exception:
            print("not a number")
            continue

        # check how far off
        error = abs(userAns - ans)
        # print how far off
        print(
            "the correct answer is = {}, your error \
             is = {} \n".format(
                ans, error
            )
        )
        numTot += 1
    error = 999
    numRight += 1


t.cancel()
