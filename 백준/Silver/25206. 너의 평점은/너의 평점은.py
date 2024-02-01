gradeDict = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}

sumofgrade=0.0
creditSum=0.0

for i in range(20):
  subject, credit, grade =input().split()

  if grade=='P':
    continue

  sumofgrade += float(credit) * gradeDict[grade]
  creditSum += float(credit)

GPA = sumofgrade/creditSum
print(GPA)