
from random import random
trials = 10000
means = []
variances = []

for y in range(1, 10):
    meanRow = []
    varianceRow = []
    for k in range(1, 10):
        p = y*0.1
        q = k*0.1
        heads = []
        for j in range(0, trials):
            numOfFlips = 0
            numOfHeads=0
            x = 1
            while(x>p):
                x = random()
                #print("x:", x)
                numOfFlips+=1
            #print("numOfFlips:",numOfFlips)
            for i in range(0, numOfFlips):
                x = random()
                if(x<q):
                    numOfHeads+=1
            heads.append(numOfHeads)
        #print("p:", p,"q:", q)
        #print(heads)
        sum = 0
        for n in heads:
            sum += n 
        mean = sum/trials
        meanRow.append(mean)
        sum = 0
        for n in heads:
            sum+=(n-mean)**2
        varianceRow.append(sum/trials)
    means.append(meanRow)
    #print(meanRow)
    variances.append(varianceRow)

#printing out values
print("mean")
print("    q:  0.1      0.2      0.3      0.4      0.5      0.6      0.7      0.8      0.9")
print(" p   -------------------------------------------------------------------------------")
for i, list in enumerate(means):
    print(f"{(i+1)*0.1:.1f} |  ", end="")
    for index, j in enumerate(list):
        if(index == 0):
            print(f"{j:.3f}", end=" ")
        else:
            if(j>=10):
                print(f"  {j:.3f}", end=" ")
            else:
                print(f"   {j:.3f}", end=" ")
    print("")
print("\nvariance")
print("    q:  0.1      0.2      0.3      0.4      0.5      0.6      0.7      0.8      0.9")
print(" p   -------------------------------------------------------------------------------")
for i, list in enumerate(variances):
    print(f"{(i+1)*0.1:.1f} |  ", end="")
    for index, j in enumerate(list):
        if(index == 0):
            print(f"{j:.3f}", end=" ")
        else:
            if(j>=10):
                print(f"  {j:.3f}", end=" ")
            else:
                print(f"   {j:.3f}", end=" ")
    print("")
