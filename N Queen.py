queen=6
nlist = [[0 for n in range(queen)] for y in range(queen)]

def nqueen(nlist, x=0):
    if all(map(any, nlist)):
        print()
        for i in nlist:
            print(i)
        return
    for c in range(x, queen):
        for r in range(queen):
            if not issafe(nlist,c,r):
                nlist[c][r]=1
                nqueen(nlist.copy(),x+1)
                nlist[c][r]=0

def issafe(nlist,c,r):
    for i in range(queen):
        if nlist[c][i]==1 or nlist[i][r]==1:
            return True 
    for k in range(queen):
        for l in range(queen):
            if k-l==c-r or k+l==c+r :
                if nlist[k][l]==1:
                    return True
nqueen(nlist)