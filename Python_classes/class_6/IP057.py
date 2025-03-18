def sum(a, b):
    rows = len(a)
    cols = len(a[0])
    
    c = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            c[i][j] = a[i][j] + b[i][j]
    
    return c


print(sum([[1,2,3],[4,5,6],[7,8,9]],
          [[1,2,3],[4,4,4],[9,8,7]]))
print(sum([[9,8,7,6,5],[4,3,2,1,0]],
          [[2,4,6,8,10],[12,14,16,18,20]]))