def dtw(X,Y):
    Lx=len(X)
    Ly=len(Y)
    path=[]
    M=[[Distance(X[i],Y[j]) for i in range(Lx)]for j in range(Ly)]
    D=[[0 for i in range(Lx+1)]for j in range(Ly+1)]
    D[0][0]=0
    for i in range(1,Lx+1):
        D[0][i]=sys.maxint
    for j in range(1,Ly+1):
        D[j][0]=sys.maxint
    for i in range(1,Ly+1):
        for j in range(1,Lx+1):
            D[i][j]=M[i-1][j-1]+min(D[i-1][j],D[i-1][j-1],D[i][j-1])
    minD=D[Ly][Lx]
    return minD