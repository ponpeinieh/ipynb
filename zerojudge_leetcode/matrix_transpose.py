def transpose(matrix): 
    rows = len(matrix)
    columns = len(matrix[0])
    # create zero filled matrix of shape (columns,rows)
    t_matrix = [[0]*rows for _ in range(columns)]
    # fill values
    for i in range(len(t_matrix)):
        for j in range(len(t_matrix[0])):
            t_matrix[i][j]= matrix[j][i]
    return t_matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j],end=" ")
        print()    

while True:
    try:   
        n,m = map(int, input().split())
        matrix=[]
        for _ in range(n):
            matrix.append(list(map(int,input().split())))
        #print(matrix)
        #print(transpose(matrix))
        t_matrix = transpose(matrix)
        print_matrix(t_matrix)
    except EOFError:
        break