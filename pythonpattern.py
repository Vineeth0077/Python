n=8
ascii1 = 65

for i in range(n):
    print((n-i-1)*" ",end=" ")
    for j in range(0,i+1):
        print(chr(ascii1),end="")
        ascii1+=1
    print()