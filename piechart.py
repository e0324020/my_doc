
subjects = ['Math', 'Science', 'English']
marks_S007 = [95, 92, 88]

plt.pie(marks_S007, labels=subjects, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99'])
plt.title("Subject-wise Marks Distribution for Student S007")
plt.show()
