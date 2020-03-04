import random

print("Question: ")

numone = random.randint(0, 100)
numtwo = random.randint(0, 11)
result = numone * numtwo

answer = int(input("{} x {} = ".format(numone, numtwo)))
print("{} x {} = {}".format(numone, numtwo, result))
print()

if answer == result:
    print("Correct")
else:
    print("Incorrect!")
