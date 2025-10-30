attendance = [95, 98, 87, 75, 96, 82, 99, 90, 78, 94]

plt.hist(attendance, bins=5, color='lightgreen', edgecolor='black')
plt.title("Distribution of Student Attendance Percentage")
plt.xlabel("Attendance Percentage Range")
plt.ylabel("Number of Students")
plt.show()
