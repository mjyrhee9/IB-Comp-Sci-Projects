# adding two matrices
A = [[10,8,19],
    [2,9,15],
    [7,11,8]]

B = [[0,4,9],
    [12,9,5],
    [17,1,8]]

def add_matrix(A,B):
    for row in range(len(A)):
        for col in range(len(B)):
            A[row][col] += B[row][col]
    return(A)

print (add_matrix(A,B))
