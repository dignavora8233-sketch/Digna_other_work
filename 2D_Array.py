print("\n1.Create and Display 3x3 Matrix")

'''
matrix = [
       [1 , 2 , 3],
       [4 , 5 , 6],
       [7 , 8 , 9]
     ]
for row in matrix:
    print(*row)

print(matrix)

'''

print("\n2.Transpose of 2 x 3 Matrix")

'''
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = []

for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transpose.append(row)

for row in transpose:
    print(*row)

'''

print("\3.Sum of all Elements")

'''
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

total = 0

for row in matrix:
    total += sum(row)

print("\nSum =", total)


'''
print("\n4.Maximum and Minimum")

'''
matrix = [
    [10, 5, 8],
    [20, 15, 2],
    [18, 25, 9]
]

maximum = matrix[0][0]
minimum = matrix[0][0]

for row in matrix:
    for value in row:
        if value > maximum:
            maximum = value
        if value < minimum:
            minimum = value

print("Maximum =", maximum)
print("Minimum =", minimum)

'''

print("\n5.Sort List using sort()")

'''
matrix = [
    [103, 78],
    [101, 85],
    [102, 92]
]

sorted_matrix = sorted(matrix, key=lambda x: x[0][0])

for row in sorted_matrix:
    print(row)

'''

print("\n6.Sort list of tuples")

students = [
      ("Amit",85),
      ("Riya",95),
      ("Jiya",69)
      ]

students = sorted(students , key = lambda X : X [1])

print(students)
