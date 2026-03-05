# Data handling and simple terminal bar chart (Python 3.12 compatible)

# Example data
names = ['sania', 'sneha', 'uvika', 'vik', 'ayra']
scores = [85, 90, 78, 92 , 68]

# Display data in console
print("Student Scores:\n")
for i in range(len(names)):
    print(f"{names[i]} scored {scores[i]} points")

# Draw a simple bar chart in terminal
print("\nBar Chart:")
max_score = max(scores)
scale = 50 / max_score  # scale bars to fit in terminal width

for i in range(len(names)):
    bar_length = int(scores[i] * scale)
    bar = '█' * bar_length
    print(f"{names[i]:<8} | {bar} ({scores[i]})")