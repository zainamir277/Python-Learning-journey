# A Python Program: Filling an empty list:
'''Make an empty list and take input from the user to fill the list.'''
# Empty List
l=[]
# taking the size of the list from the user:
s=int(input("Enter size of list : "))
# Using a For Loop to add values in List: 
for i in range (s):
    n=int(input(f"Enter value of index {i} : "))
    l.append(n)
# Print the list:
print(l)