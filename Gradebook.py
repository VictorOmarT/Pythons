last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

subjects = ["physics", "calculus", "poetry", "history" ]

grades = [98, 97, 85, 88]

subjects.append("Computer science")
grades.append(100)

gradesbook = list(zip(subjects, grades))
gradesbook.append(("visual arts",93))
#print(list(gradesbook))

full_gradebook = list(zip(last_semester_gradebook, gradesbook))

print(full_gradebook)

