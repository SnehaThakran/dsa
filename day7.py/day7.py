# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))
# matrix = []
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         value = int(input(f"Enter element at position ({i}, {j}): "))
#         row.append(value)
#     matrix.append(row)
# print(matrix)
# #to traversal the matrix
# for i in range(rows):
#     for j in range(cols):
#         print(matrix[i][j], end=" ")
#     print()
#traversal - visitng each element of the matrix/loop through each element of the matrix/array  
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))  
matrix = []
for i in range(rows):   
    row = []
    for j in range(cols):
        value = int(input(f"Enter element at position ({i}, {j}): "))
        row.append(value)
    matrix.append(row)  
#rowise traversal   
# for i in range(rows):
#     for j in range(cols):
#         print(matrix[i][j], end=" ")
#     print()
#columnwise traversal
# for j in range(cols):
#     for i in range(rows):
#         print(matrix[i][j], end=" ")
#     print()
#  traversal of primary diagonal
# for i in range(rows):
#     print(matrix[i][j], end="")
#  traversal of secondary diagonal
# for i in range(rows):
#     print(matrix[i][cols - 1 - i], end="")

# write a program to calculate sum of each row individually
# for i in range(rows):
#     row_sum = 0       
#     for j in range(cols):
#         row_sum += matrix[i][j]
#     print(f"Sum of row {i}: {row_sum}")

# to print upper triangle of matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  
for i in range(len(matrix)):
    for j in range(i, len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()
# to print lower triangle of matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix)):    
    for j in range(i + 1):
        print(matrix[i][j], end=' ')
    print()



