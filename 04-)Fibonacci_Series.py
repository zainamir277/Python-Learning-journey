# Python Program: Fibonacci series
''' Take input from the user and find the Fibonacci series upto that index.'''
# take input from user
n=int(input("Enter number to find fabonacci of : "))
# print first two values of the Fibonacci series
a,b=0,1
print(a)
print(b)
# using a for loop to print the resting values of the Fibonacci series
for i in range (1,n):
    c=a+b
    print(c)
    a,b=b,c