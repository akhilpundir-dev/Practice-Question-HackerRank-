# Student average marks
import random 

student_marks = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

query_name = random.choice(list(student_marks.keys()))

avg_marks = 0

for key, value in student_marks.items():
    if key == query_name:
        total_marks = 0

        for i in value:
            total_marks += i

        avg_marks = total_marks / 3

print(f"{avg_marks:.2f}")