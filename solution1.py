
myString = "How do you fix API Msn Win CRT convert 1110 dill is missing from your computer"

counterDict = {}

for i in myString:
    
    if i in counterDict:
        counterDict[i] += 1
    else:
        counterDict[i] = 1

print(counterDict)