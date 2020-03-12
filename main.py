import subprocess
from question import quickMath

correct_ct = 0

print("Solve 3 question correctly for breaking the question loop")
print()

while correct_ct < 3:
    print("No. {}".format(correct_ct + 1))
    correct = quickMath(correct_ct)
    print("---------------------------")

    if correct:
        print("Correct")
        correct_ct += 1
        print("{}/3".format(correct_ct))
    else:
        print("Incorrect!")
        print("{}/3".format(correct_ct))
    print()
    print()

print("Executing next script >>>")
theproc = subprocess.Popen("script_to_execute.py", shell = True)
theproc.communicate()      
