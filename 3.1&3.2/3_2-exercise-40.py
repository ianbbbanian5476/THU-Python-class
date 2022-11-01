gpa = eval(input("Enter your gpa: "))
if gpa >= 3.9:
    honors = " summa cum laude."
else:
    if gpa >= 3.6:
        honors = " magna cum laude."
    else:
        if gpa >= 3.3:
            honors = " cum laude."
        else:
            honors = "."
print("You graduated" + honors)