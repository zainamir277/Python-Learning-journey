# A Python program: Pass/Fail Program
'''If the student's percentage is greater than or equal to 50% and attendance is greater than or equal to 80%, then the student passes.
If attendance is less then 80% but the percentage is greater then 50%, then add 10% to his/her attendance.Now if attendance
is greater then 80%, then he/she passes.
If his/her percentage is less then 50%, then he/she fails.
 '''

# Take input from user:
obtmarks=int(input("Enter obtained marks : "))
totalmarks=int(input("Enter total marks : "))
# Calculate percentage
percentage=(obtmarks/totalmarks)*100
print(f"{percentage}%")

attendance=int(input("Enter your attendance : "))
print(f"{attendance}%")
# In the first conditional statement, pass or fail based on the percentage 
if percentage>=50 and attendance>=80:
    print("Congrats! You are pass")
    print(f"Your percentage is {percentage}")
    print(f"Your attendance is {attendance}")
# Now, if the percentage is good but the attendance is low, then add grace attendance
elif percentage>=50 and attendance<80:
    attendance+=10
    # After grace attendance, if attendance becomes satisfactory, then pass
    if attendance>=80:
        print("Congrats! You are pass but with grace attendance")
        print(f"Your percentage is {percentage}")
        print(f"Your grace attendance is {attendance}")
    # Otherwise fail
    else:
        print("Sorry! You are fail due to shortage of attendance")
        print(f"Your percentage is {percentage}")
        print(f"Your grace attendance is {attendance}")
# if the percentage is not satisfactory, then no need to go into depth of the result
else:
    print("Sorry! You are failed due to low percentage")