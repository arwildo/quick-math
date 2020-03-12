import random


def quickMath(correct_ct):
    numone = random.randint(0, 100)
    numtwo = random.randint(0, 11)
    result = numone * numtwo

    answer = int(input("Question: {} x {} = ".format(numone, numtwo)))
    print("Result: {} x {} = {}".format(numone, numtwo, result))

    if answer == result:
        return True
    else:
        return False


if __name__ == "__main__":
    correct_ct = 0

    print("Solve 3 question break from question loop")
    print()

    while correct_ct <= 3:
        correct = quickMath()
        print("---------------------------")

        if correct:
            print("Correct")
            print("{}/3".format(correct_ct))
            correct_ct += 1
        else:
            print("Incorrect!")
            print("{}/3".format(correct_ct))
        print()
        print()
