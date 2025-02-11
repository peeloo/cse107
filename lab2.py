from random import random

print("---------------------------------------------")
print(" #azure  #carmine  proportion ending in azure")
print("---------------------------------------------")
trials = 2000

for i in range(1, 6):
    azureWin = 0

    for z in range(trials):
        total = 100
        azure = i*10
        carmine = total - azure

        chStart = True
        chColor = "none"
        while total > 1:
            if chStart:
                p = azure/(azure + carmine) #prob of azure
                x = random()
                if x < p:
                    chColor = "azure"
                    azure -= 1
                    total -= 1
                else:
                    chColor = "carmine"
                    carmine -= 1
                    total -= 1
                #print("chapter start color:", chColor)
                chStart = False
            if total == 1: #if ch started at last ball, quit out
                break

            p = azure/(azure + carmine) #prob of azure
            x = random()
            if x < p:
                ball = "azure"
                #print(ball)
                if ball != chColor:
                    chStart = True
                else:
                    azure -= 1
                    total -= 1
            else:
                ball = "carmine"
                #print(ball)
                if ball != chColor:
                    chStart = True
                else:
                    carmine -= 1
                    total -= 1

        #print("final azure:", azure)
        #print("final carmine:", carmine)
        if azure != 0:
            azureWin += 1
            #print("azureWin!")

    relFreq = azureWin/trials
    print("  ", i*10, "\t  ", 100 - i*10, "\t   ", f"{relFreq:.4f}") 
