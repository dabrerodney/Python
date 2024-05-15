num=int(input("Enter Number:"))
n=num
fact=1
if num< 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0 or num == 1:
    print("The factorial of",n, "is 1")
else:
    while num >=2:
       fact=fact*num
       num-=1
    print("The factorial of ",n," is ",fact)