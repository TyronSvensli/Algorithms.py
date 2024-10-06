import random
import pickle

matrix = []
x = 0
y = 0
score = 0

def matrixprint():
    for row in range(Row):
        for column in range(Column):
            print(matrix[row][column], end="\t")
        print("\n")

def matrix_gen():
    if blockades == "y":
        for row in range(Row):    
            temp_list = []
            for column in range(Column):   
                temp_number = random.randint(0, 11)
                if temp_number >= 11:
                    if row != 0 and column != Column:
                        if matrix[row-1][column]:
                            temp_list.append(random.randint(0, 10))
                    if row == 0 and column == 0:
                        temp_list.append(random.randint(0, 10))
                    elif row == Row -1:
                        temp_list.append(random.randint(0, 10))
                    else:
                        temp_list.append("❌")
                else:
                    temp_list.append(temp_number)
            matrix.append(temp_list)
        matrixprint()
    else:
        for row in range(Row):    
            temp_list = []
            for column in range(Column):   
                temp_list.append(random.randint(0, 10))
            matrix.append(temp_list)
        matrixprint()
    return matrix

def advanced_algroithm(x, y, score):
    while x < Row or y < Column -1:
        score += matrix[x][y]
        matrix[x][y] = "⬜️"
        matrixprint()
        print("score is: ", str(score))
        print("X: "+str(x+1), "Y: "+str(y+1),"\n")
        try:
            right_1 = matrix[x][y+1] if y+1 < Column and matrix[x][y+1] != "❌" else -1
            down_1 = matrix[x+1][y] if x+1 < Row and matrix[x+1][y] != "❌" else -1
            right_2 = matrix[x][y+2] if y+2 < Column and matrix[x][y+2] != "❌" else -1
            down_2 = matrix[x+2][y] if x+2 < Row and matrix[x+2][y] != "❌" else -1
            right_sum = (right_1 if right_1 != -1 else 0) + (right_2 if right_2 != -1 else 0)
            down_sum = (down_1 if down_1 != -1 else 0) + (down_2 if down_2 != -1 else 0)

            if right_sum >= down_sum and right_1 != -1:
                y += 1
            elif down_1 != -1:
                x += 1
            else:
                if y < Column - 1:
                    y += 1
                else:
                    x += 1
        except IndexError:
            if y < Column - 1:
                y += 1
            else:
                x += 1

def greedy_algroithm(x, y, score):
    while x < Row or y < Column -1:
        score += matrix[x][y]
        matrix[x][y] = "⬜️"
        matrixprint()
        print("score is: ", str(score))
        print("X: "+str(x+1), "Y: "+str(y+1),"\n")
        try:
            if matrix[x][y+1] == "❌":
                x += 1
            elif matrix[x+1][y] == "❌":
                y += 1
            elif matrix[x+1][y] >= matrix[x][y+1]:
                x += 1
            else:
                y += 1
        except IndexError:
            if y < Column -1:
                y += 1
            else:
                x += 1

def save(matrix):
    filnavn = input("What do you want to name the file?: ")
    f = open(filnavn, "wb")
    pickle.dump(matrix, f)

def load():
    filnavn = input("What is the name of the file you want to load?: ")
    f = open(filnavn, "rb")
    matrix = pickle.load(f)
    return matrix

loading = input("Do you want to load a matrix or generate a new one, write 'load' to load, just press ENTER to generate a new one: ").lower()
if loading == "load":
    matrix = load()
else:
    Row = int(input("How many rows?: "))
    Column = int(input("How many columns?: "))
    blockades = input("Do you want blockades? y/n: ").lower()
    matrix = matrix_gen()
    lagring = input("Do you want to save this matrix? y/n: ").lower()
    if lagring == "y":
        save(matrix)

Row = len(matrix)
Column = len(matrix[0]) if Row > 0 else 0

algroithm = input("Do you want to use the two-step algorithm? y/n: ").lower()   
if algroithm == "y":
    advanced_algroithm(x, y, score)
else:
    greedy_algroithm(x, y, score)