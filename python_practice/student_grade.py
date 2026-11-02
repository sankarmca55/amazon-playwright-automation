# marks = int(input("Enter the student marks:"))

# if marks >= 90:
#     print(f"Grade A {marks}")
# elif marks >= 75:
#     print(f"Grade B {marks}")
# elif marks >=60:
#     print(f"Grade C {marks}")
# elif marks >=35:
#     print(f"Grade D {marks}")
# else:
#     print("Faill")


# Program Explanation
# 1. User must enter 5 different values and store it in separate variables.
# 2. Then sum up all the five marks and divide by 5 to find the average of the marks.
# 3. If the average is greater than 90, “Grade: A” is printed.
# 4. If the average is in between 80 and 90, “Grade: B” is printed.
# 5. If the average is in between 70 and 80, “Grade: C” is printed.
# 6. If the average is in between 60 and 70, “Grade: D” is printed.
# 7. If the average is anything below 60, “Grade: F” is printed.

sub1 = int(input("Enter marks for the first subject: "))
sub2 = int(input("Enter marks for the second subject: "))
sub3 = int(input("Enter marks for the thried subject: "))
sub4 = int(input("Enter marks for the fourth subject: "))
sub5 = int(input("Enter marks for the fifth subject: "))

avg = (sub1+sub2+sub3+sub4+sub5) / 5


if avg >= 90:
    print(f"Grade A {avg}")
elif avg >= 80 and avg< 90:
    print(f"Grade B {avg}")
elif avg >= 70 and avg < 80:
    print(f"Grade C {avg}")
elif avg >= 60 and avg < 70:
    print(f"Grade D {avg}")
else:
    print(f"Grade F")