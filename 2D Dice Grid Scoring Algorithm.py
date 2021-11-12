# 2D Dice Grid Scoring Algorithm

from random import randint

greid = []


def genrateGrid():
    global greid
    greid = []
    for row in range(4):
        greid.append([])
        for col in range(4):
            dice = randint(1, 6)
            greid[row].append(dice)


def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False


def isOdd(number):
    if number % 2 != 0:
        return True
    else:
        return False


def display_grid():
    global greid
    for row in range(4):
        st = " | "
        for col in range(4):
            st = st + str(greid[row][col]) + " | "
        print(st)


genrateGrid()
display_grid()
score = 0

if isEven(greid[0][0]) and isEven(greid[0][3]) and isEven(greid[3][0]) and isEven(greid[3][3]):
    print(f"Four even corner! +20pts")
    score += 20

if isOdd(greid[0][0]) and isOdd(greid[0][3]) and isOdd(greid[3][0]) and isOdd(greid[3][3]):
    print("Four odd corner! + 20pts")
    score += 20

if isEven(greid[0][0]) and isEven(greid[1][1]) and isEven(greid[2][2]) and isEven(greid[3][3]):
    print("Four even at diagonal! +20pts")
    score += 20

if isOdd(greid[0][0]) and isOdd(greid[1][1]) and isOdd(greid[2][2]) and isOdd(greid[3][3]):
    print("Four odd at diagonal! + 20pts")
    score += 20

print(f"\nGrid Score: {score}pts")
