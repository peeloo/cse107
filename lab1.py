from random import random

trials = 1000
n = 300
p = 0.5
bobWins = 0

for i in range(trials):
    bobHeads = 0
    for j in range(n+1):
        flip = random()
        if flip < p:
            bobHeads += 1

    aliceHeads = 0
    for j in range(n):
        flip = random()
        if flip < p:
            aliceHeads += 1
    
    if bobHeads > aliceHeads:
        bobWins+=1

rFreq = bobWins/trials
print("n:", n)
print("Trials:", trials, "\n")

print(f"Fair coin (p = {p})")
print("Number of Times Bob tossed more heads: ", bobWins)
print("Number of Times Alice tossed more heads: ", 1000-bobWins)
print("Relative frequency:", rFreq, "\n")

print("Loaded coin:")
print("Bob trials:", n+1)
print("Alice trials:", n)
print("--------------------------")
print("p\trelative frequency")
print("--------------------------")

p = 0.2

for i in range(1, 8):
    bobWins = 0
    for j in range(trials):

        bobHeads = 0
        for k in range(n+1):
           x = random()
           if x < p:
               bobHeads += 1

        aliceHeads = 0
        for i in range(n):
           x = random()
           if x < p:
               aliceHeads += 1

        if bobHeads > aliceHeads:
            bobWins+=1

    rFrequency = bobWins/trials
    print(p,"\t", rFrequency) 
    p += 0.1
    p=round(p, 1)


