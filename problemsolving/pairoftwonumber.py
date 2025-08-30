i=int(input())
o=int(input())
if i % 3==0 and o % 3==0 and (i % 12==0 or o % 12==0):
    print("both")
else:
    print("none")
