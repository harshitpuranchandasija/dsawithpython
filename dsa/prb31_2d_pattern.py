from prb29_2d_matrix import matrix,rows,cols

print("*" * 10, " INPUT ","*" * 10)

for i in range(0,rows):
    for j in range(0,cols):
        print(matrix[i][j],end = " ")
    print()

print("*" * 10, " PATTERN STARTED ","*" * 10)

print("Printing Diagonals")

for i in range(0,rows):
    for j in range(0,cols):
        if i == j:
            print(matrix[i][j],end = " ")
        else:
            print("*",end = " ")
    print()

print("*" * 10)
for i in range(0,rows):
    for j in range(0,cols):
        if i + j == cols - 1:
            print(matrix[i][j],end = " ")
        else:
            print("*",end = " ")
    print()

print("*" * 10)
for i in range(0,rows):
    for j in range(0,cols):
        if j >=i:
            print(matrix[i][j],end = " ")
        else:
            print("*",end = " ")
    print()

print("*" * 10)
for i in range(0,rows):
    for j in range(0,cols):
        if i >=j:
            print(matrix[i][j],end = " ")
        else:
            print("*",end = " ")
    print()

print("*" * 10)
for i in range(0,rows):
    for j in range(0,cols):
        if ((i + j) %2) == 0:
            print(matrix[i][j],end = " ")
        else:
            print("*",end = " ")
    print()

print("*" * 10)
for i in range(0,rows):
    for j in range(0,cols):
        if ((i + j) %2) != 0:
            print(matrix[i][j],end = " ")
        else:
            print("*",end = " ")
    print()