import subprocess
from question import quickMath

correct_ct = 1

print("Solve 3 question break from question loop")
print()

while correct_ct < 4:
    correct = quickMath(correct_ct)
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

print("Executing next script >>>")
theproc = subprocess.Popen("script_to_execute.py", shell = True)
theproc.communicate()      
