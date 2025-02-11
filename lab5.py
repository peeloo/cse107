from random import random
import math
array = [0]*101
trials = 20000
totalTrials = 0

for i in range(0, trials):
    y1 = random()
    #print(y1)
    y1 = math.log(1.0/(1.0-y1))

    y2 = random()
    y2 = math.log(1.0/(1.0-y2))

    z = y1+y2
    x = math.floor(z*10) + 1
    if(z < 10):
        #print(z)
        #print(x)
        totalTrials+=1
        array[x]+=1

#perform sum up
index = 1
for j in range(0,10):
    for i in range(0,10):
        array[index] += array[index-1] 
        index +=1


print("Sum of Exponentials CDF:")
print("         .0      .1      .2      .3      .4      .5      .6      .7      .8      .9")
print("      --------------------------------------------------------------------------------")

index = 0
for j in range(0, 10):
    print(str(j)+".0 |", end = "  ")
    for i in range(0, 10):
        print(f"{array[index]/trials:.4f}", end = "  ")
        index+=1
    print("")
