# Python Program: Even/Odd and prime numbers
''' Take input of range from user and write a Python program to find Even/Odd and prime numbers'''
# Take input from user:
start=int(input("Enter start of range : "))
end=int(input("Enter end of range : "))
# Take variables with zero value to calculate the total number of Even/Odd and Prime numbers.
even=0
odd=0
prime=0
# Use for Loop to run a range of numbers:
for n in range(start,end+1):
# Separate Even and Odd numbers using remainder logic.
    if n%2==0:
        print(f"{n} is an even number")
        even+=1
    else:
        print(f"{n} is an odd number")
        odd+=1
# Find Prime numbers
    isprime=0
    if n==1:
        continue
    else:
        for i in range (2,n):
            if n%i==0:
                isprime=1
        if isprime==0:
                print(f"{n} is a prime number")
                prime+=1
# Calculate Total Even/Odd/Prime numbers.
print(f"Total even numbers are {even}")
print(f"Total odd numbers are {odd}")
print(f"Total prime numbers are {prime}")