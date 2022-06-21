number=int(input('\n\t Enter Decimal Number = '))
temp=number
binarynumber=""
while number>0 :
    rem=number%2
    binarynumber+=str(rem)
    number=number//2
print("\n\t The binary equivalent of",str(temp),"is",binarynumber[::-1])