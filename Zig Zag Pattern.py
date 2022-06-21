number=min(int(input() or 10), 10)
value=map('{:3}'.format,range(0,number*number))
Matrix=[[0]*number
    for _ in range(number) ]
d=[[*zip(range(k),range(k) [::-1])]
   for k in range(1,number+1)] +\
   [[*zip(range(k,number),range(k,number)[::-1])]
    for k in range(1,number)]
for k in range(2*number-1):
    index=d[k][::[-1,1][k%2]]
    for row,column in index:
        Matrix[row][column]=next(value)
        
for row in Matrix: print(*row,'\n')