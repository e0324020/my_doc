import matplotlib.pyplot as plt

students = ['S001', 'S002', 'S003', 'S004', 'S005', 'S006', 'S007', 'S008', 'S009', 'S010']
math_marks = [85, 92, 78, 65, 88, 72, 95, 81, 70, 89]

plt.bar(students, math_marks, color='lightblue')
plt.title("Math Marks Comparison Across Students")
plt.xlabel("Student ID")
plt.ylabel("Math Marks")
plt.xticks(rotation=45)
plt.show()
