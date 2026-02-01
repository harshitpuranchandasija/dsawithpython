from prb29_2d_matrix import matrix,rows,cols

#matrix is 2d array/list
sum=0

for i in range(0,rows):
    for j in range(0,cols):
        print(matrix[i][j])
        sum +=matrix[i][j]

print("Sum of 2D matrix is",sum)