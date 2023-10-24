# Using Nested if -else statements to create a simple academic-grade-calculator

grade = 90



if grade >= 90:
    if grade >= 97:
        print(str(grade) + ' = A+')
    elif grade >= 93:
        print(str(grade) + ' = A')
    else:
        print(str(grade) + ' = A-')
        
elif grade >= 80:
    if grade >= 87:
        print(str(grade) + ' = B+')
    elif grade >= 83:
        print(str(grade) + ' = B')
    else:
        print(str(grade) + ' = B-')
        
elif grade >= 70:
    if grade >= 77:
        print(str(grade) + ' C+')
    elif grade >= 73:
        print(str(grade) + ' C')
    else:
        print(str(grade) + ' C-')
    
    

