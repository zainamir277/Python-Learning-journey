# A Python Program: Max Marks Finder
'''Write a function to find the top three students in the given dictionary.'''
# make a function:
def topmarks(dict2):
    print("Top three students are :")
# use for loop to find top three students:
    for i in range(3):
        maxkey=""
        maxvalue=-1
# use for loop to find max marks:
        for k in dict2.keys():
            if maxvalue<dict2[k]:
                maxkey=k
                maxvalue=dict2[k]
# print Name of student and max marks
        print(f"{maxkey}:{maxvalue}")
# remove the top marks from the dictionary to find the next highest number:
        dict.pop(maxkey,maxvalue)