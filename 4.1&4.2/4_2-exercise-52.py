grade = []
for i in range(5):
    grade.append(int(input(f'Enter grade {i+1}: ')))
for j in range(2):
    grade.remove(min(grade))
print(f'Range: {max(grade) - min(grade)}\nAverage: {int(sum(grade) / len(grade))}')
