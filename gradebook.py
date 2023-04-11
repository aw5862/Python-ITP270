#!/bin/python3
subjects = ["physics","calculus","poetry","history"]
grades = [98,97,85,88]
gradebook = []

#Create Some Lists:

for i in range(len(subjects)):
	gradebook.append([subjects[i],grades[i]])
print(gradebook)

#Add More Subjects:

gradebook.append(["computer science",100])
gradebook.append(["visual arts", 93])

#print(gradebook)

#Modify The Gradebook:

#add 5 points to visual arts
for subject in gradebook:
	if subject[0] == "visual arts":
		subject[1] += 5

#Pass/Fail poetry
for subject in gradebook:
	if subject[0] == "poetry":
		subject.remove(85)
		subject.append("Pass")
#print(gradebook)

#One Big Gradebook!
last_semester_gradebook = ["your grades from last semester"]
full_gradebook = gradebook + last_semester_gradebook

print(full_gradebook)
