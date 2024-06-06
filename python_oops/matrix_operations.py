
X = [[12, 34, 56, 14, 18, 19, 23], 
     [21, 43, 65, 41, 81, 91, 32], 
     [6, 10, 17, 15, 13, 29, 33]]

# count the number of rows
num_rows = len(X)

# count the number of columns

num_col = len(X[0] if num_rows > 0 else 0 )

# print(X[1])

print(f'The number of rows are: {num_rows}')
print(f'The number of columns are: {num_col}')
