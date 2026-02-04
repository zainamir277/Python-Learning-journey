# A Python program: Grading System
''' Ask the user to enter the obtained and total marks. Your program has to calculate its percentage and grade, such as :
If the percentage is:
<50   = F
50-60 = D
60-70 = C
70-80 = B
80-90 = A
90-100= A+'''
# Take input from user:
obtmarks=int(input("Enter obtained marks : "))
totalmarks=int(input("Enter total marks : "))
# Filter the possible invalid inputs: 
if (obtmarks < 0 or totalmarks <= 0 or obtmarks > totalmarks):
    print("You entered invalid input")
# After filtering, start calculating Grades:
else:
    percentage=(obtmarks/totalmarks)*100
    print(f"Your percentage is {percentage}")
    if 100>=percentage>=90:
        print("Congrats! Your grade is A+")
    elif 90>percentage>=80:
        print("Congrats! Your grade is A")
    elif 80>percentage>=70:
        print("Congrats! Your grade is B")
    elif 70>percentage>=60:
        print("Congrats! Your grade is C")
    elif 60>percentage>=50:
        print("Congrats! Your grade is D")
    elif percentage<50:    
        print("Sorry! Your grade is F")