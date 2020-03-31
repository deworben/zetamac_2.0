import time
from random import seed
from random import random

from threading import Timer

# seed random number generator
seed(10)
start = time.time()
gameTime = 4
errorTot = 0
userAns = 0


def runKill():

    for i in range(20):
        print(".")
    print("Game is over, wit total error = " + str(errorTot))
    for i in range(10):
        print(".")


# t = Timer(gameTime, print, ['Sorry, times up'])
t = Timer(gameTime, runKill)


def makeNum():
    temp = int(random() * 50)
    if temp == 0:
        return 1
    else:
        return temp


t.start()
while True:
    # create question
    num1 = makeNum()
    num2 = makeNum()

    # test-----
    # making num2 smaller
    while num2 <= num1:
        num2 = makeNum()
    # create answer
    ans = 100 * num1 / num2
    # user input answer
    userAns = input("what is {} as a percentage of {}\n".format(num1, num2))
    try:
        userAns = float(userAns)
    except Exception:
        print("not a number")
        continue

    # user_input = get_user_input('please insert something:', 2)

    # check how far off
    error = abs(userAns - ans)
    # print how far off
    print("the correct answer is = {}, your error is = {} ".format(ans, error))
    # add total error amount to sum
    errorTot += error


t.cancel()
