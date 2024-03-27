def stepConvert(X, Y):
    m = len(X)
    n = len(Y)

    sc = [[0 for r in range(n + 1)] for r in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                sc[i][j] = j
            elif j == 0:
                sc[i][j] = i
            elif X[i - 1] == Y[j - 1]:
                sc[i][j] = sc[i - 1][j - 1]
            else:
                sc[i][j] = 1 + min(sc[i - 1][j - 1], sc[i][j - 1], sc[i - 1][j])

    return sc[m][n]

X = "abad"
Y = "abac"
print(stepConvert(X, Y))  

X = "Insa"
Y = "India"
print(stepConvert(X, Y))  
