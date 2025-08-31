import matplotlib.pyplot as plt

# Dataset: [Hours Studied, Sleep Hours, Pass/Fail]
students = [
    [1.0, 5.0, 0],
    [2.0, 5.5, 0],
    [3.0, 6.0, 0],
    [4.5, 5.0, 0],
    [5.0, 6.5, 1],
    [5.5, 7.0, 1],
    [6.0, 6.0, 1],
    [7.0, 7.0, 1],
    [8.0, 6.0, 1],
    [9.0, 7.5, 1]
]

# New student
new_student = [4.0, 6.0]

# Separate points by Pass/Fail
fail_points = [s for s in students if s[2] == 0]
pass_points = [s for s in students if s[2] == 1]

# Plot Fail (blue circles)
plt.scatter([p[0] for p in fail_points], [p[1] for p in fail_points],
            color='blue', marker='o', label='Fail (0)')

# Plot Pass (red squares)
plt.scatter([p[0] for p in pass_points], [p[1] for p in pass_points],
            color='red', marker='s', label='Pass (1)')

# Plot new student (gold star)
plt.scatter(new_student[0], new_student[1], color='gold', marker='*', s=200, label='New Student')

# Labels and title
plt.xlabel('Hours Studied (X1)')
plt.ylabel('Sleep Hours (X2)')
plt.title('KNN Classification (k=3)')
plt.legend()
plt.grid(True)

# Show plot
plt.show()
