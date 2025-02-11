def printMatrix(M):
    print("  y:   0      1      2      3      4      5      6      7")
    print("x-----------------------------------------------------------")
    a = 0
    for i in M:
        print(a, "| ", end="")
        for j in i:
            print(f"{j:.4f}", end=" ")
        a += 1
        print("")

from random import random

trials = 100000
n = 7 # number of weeks
p = 0.6 # probability of playing this week
q = 0.7 # probability of winning

joint = [[0] * (i + 1) for i in range(8)] # Initialize joint PMF matrix with variable row sizes

# Run trials to populate joint PMF
for _ in range(trials):
    y = 0 # number of wins
    x = 0 # number of plays
    for i in range(n):
        if random() < p: # Will Joe play this week?
            x += 1
            if random() < q: # Will Joe win?
                y += 1
    joint[x][y] += 1 # increment (x, y) at end of week

# Perform relative frequency calculation
for row, i in enumerate(joint):
    for col in range(len(i)):
        joint[row][col] = joint[row][col] / trials

print("Joint PMF of X and Y")
printMatrix(joint)

# Calculate marginals for X and Y
marginalx = [sum(i) for i in joint]  # Marginal for X (sum over rows)
marginaly = [0] * 8
for row in range(len(joint)):
    for col in range(len(joint[row])):
        marginaly[col] += joint[row][col]  # Marginal for Y (sum over columns)

# Calculate Conditional PMF of X given Y
xGivenY = [[0] * (i + 1) for i in range(8)]
for row in range(len(joint)):
    for col in range(len(joint[row])):
        if marginaly[col] != 0:
            xGivenY[row][col] = joint[row][col] / marginaly[col]
print("\nConditional PMF of X given Y")
printMatrix(xGivenY)

# Calculate Conditional PMF of Y given X
yGivenX = [[0] * (i + 1) for i in range(8)]
for row in range(len(joint)):
    for col in range(len(joint[row])):
        if marginalx[row] != 0:
            yGivenX[row][col] = joint[row][col] / marginalx[row]
print("\nConditional PMF of Y given X")
printMatrix(yGivenX)
