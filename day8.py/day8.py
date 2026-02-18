#90
matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

rows = len(matrix)
cols = len(matrix[0])

transpose = []
for r in range(cols):
    row = []
    for c in range(rows):
        row.append(matrix[c][r])
    transpose.append(row)

for c in range(len(transpose[0])):
    top = 0
    bottom = len(transpose) - 1
    while top < bottom:
        transpose[top][c], transpose[bottom][c] = transpose[bottom][c], transpose[top][c]
        top += 1
        bottom -= 1

for row in transpose:
    print(row)

#tranpose of matrix
for r in range(rows):
    for c in range(cols):
        transpose[c][r]=matrix[r][c]

#2.reverse each row
for r in range (rows):
    transpose[r].reverse()
    print(transpose)

# rotate 90 degree anti-clock wise

matrix=[[1,2,3],[4,5,6]]
row=len(matrix)
col=len(matrix[0])
tRow =col
tCol= row
tranpose =[]
for r in range(col):
    rowArr=[]
    for c in range(row):
     transpose.append(row)
   
print(transpose)
 
for r in range(rows):
    for c in range(cols):
        transpose[c][r]=matrix[r][c]