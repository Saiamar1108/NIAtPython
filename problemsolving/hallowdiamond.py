n=int(input())


for i in range(1,n+1):
  space =2(n-i)
  print(("    "*space)+("*"*(i))+("    "*space))
for i in range (n-1,0,-1):
    space =((n-i))
    print(("    "*space)+(" *  "*(2*(i)-1))+("    "*space))  