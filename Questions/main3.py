# Second lowest grade
student=[["alpha",30],["beta",40],["gamma",50],["theta",30],["lambda",90]]

students=[]
for name,score in student:
    students.append([name,score])

        

grade=[student[1] for student in students]
unique_grade=sorted(set(grade))
second_lowest=unique_grade[1]
name_score=[]
for i in students:
    if i[1]==second_lowest:
        name_score.append(i[0])
name_score.sort()
for i in name_score:
    print(i)
