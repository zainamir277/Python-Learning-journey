# A Python Program: Min Marks Finder
''' Write a function to find the lowest 2 students from each class.'''
# Make a function:
def min2(dict3):
# Take total marks from user to find min marks:
    minvalue=int(input("Enter total marks :"))
    print ("Lowest 2 students are:")
    minkey=""
# Use a for loop to find the lowest 2 marks:
    for i in range(2):
# use for loop to find min marks:
        for k in dict3.keys():
            if minvalue>dict3[k]:
                minkey=k
                minvalue=dict3[k]
# print lowest marks:
        print(f"Lowest marks is of {minkey} : {minvalue}")
# remove lowest marks to find next lowest marks:
        dict.pop(minkey,minvalue)