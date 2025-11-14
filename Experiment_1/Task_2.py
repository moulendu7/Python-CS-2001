n = int(input("Enter number of subjects: "))
marks = []
for i in range(n):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)
avg = sum(marks) / n
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"
print("\nAverage Marks:", avg)
print("Grade:", grade)