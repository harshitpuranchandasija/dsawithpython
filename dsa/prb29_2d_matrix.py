matrix = [[0,1,2],[3,4,5],[6,7,8]]

#Calculate number of rows and columns
rows = len(matrix)
cols = len(matrix[0])

for i in range(0,rows):
    for j in range(0,cols):
        print(matrix[i][j],end = " ")
    
    print()