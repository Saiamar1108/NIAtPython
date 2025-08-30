a=int(input())
if a%5==0 and a%10==0:
    print("Divisible by 10")
elif a%5==0:
    print("Divisible by 5")
else:
    print("Not divisible by 5 or 10") 