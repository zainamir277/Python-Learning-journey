# A Python Program : Even/Odd Program:
"""Take input from user and find weather the range (1-n) is Even or Odd"""

# Take Input from User
n=int(input("Enter range of numbers : "))
# Filter invalid inputs
if n<=0:
    print("Please enter a positive number")
else:
# To calculate total even/odd take 0 verialbe value which increase with every even/odd entry:
    even=0
    odd=0
# Apply For Loop to find Even and Odd :
    for i in range(1,n+1):
# Separate even numbers:
        if i%2==0:
            even+=1
            print(f"{i} is an even number")
# Separate odd numbers:
        else:
            odd+=1
            print(f"{i} is an odd number")
    print(f"Total even numbers are {even}")
    print(f"Total odd numbers are {odd}")