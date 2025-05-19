import time
gap = time.sleep
print("📊 Gpa calculator")
gap(1)
marks= []
subs = int(input("Enter the numbers of subjects:"))
for i in range(subs):
    grade =input("Enter grade (A+/D):")
    if (grade=="A+"):
        marks.append(4)
    elif (grade=="A"):
            marks.append(3.6)
    elif (grade=="B+"):
            marks.append(3.2)  
    elif (grade=="B"):
            marks.append(2.8) 
    elif (grade=="C+"):
            marks.append(2.4) 
    elif (grade=="C"):
            marks.append(2)  
    elif (grade=="D+"):
            marks.append(1.6)      
    elif (grade=="D"):
            marks.append(1.2)  
    else:
           marks.append(0)                                                          

total_marks= sum(marks)
no_of_subjects = len(marks)
gpa = total_marks / no_of_subjects

print("Loading...", end='', flush=True)
gap(2)
print(f"\rYou scored {gpa} Gpa\r", end='', flush=True)
gap(5)