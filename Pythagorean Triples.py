from math import gcd
n1=int(input('\n\t Enter first number = '))
n2=int(input('\n\t Enter second number = '))
print('\n\t Primitive Pythagorean Triples between ',n1,'and ',n2,'are as below :-')
if n1>n2:
    n1,n2=n2,n1
if n1<3:
    n1=3
if n1==n2 or n2<5:
    print('\n\tWrong Input')
else:
    b,i=1,0
    a=b-1
    f=True
    while 1:
        a+=2
        if gcd(a,b)!=1:
            continue
        p,q=2*a*b,a**2-b**2
        if p>q:
            p,q=q,p
        if p<n1:
            f=True
            continue
        r=a**2+b**2
        if r<=n2 and p>=n1:
            i+=1
            f=True
            print('\n\t Triplet No ',i,'\t Pair of Pythagorean Triples - ',(p,q,r))
        elif f:
            b+=1
            a=b-1
            f=False
        else:
            break