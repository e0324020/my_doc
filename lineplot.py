subjects = ['Math', 'Science', 'English']
avg_marks = [81.5, 80.8, 82.9]  

plt.plot(subjects, avg_marks, marker='o', linestyle='-', color='orange')
plt.title("Average Marks Trend Across Subjects")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.grid(True)
plt.show()
