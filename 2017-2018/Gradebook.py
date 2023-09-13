import math
def computeGrade(num_stu, num_assign, raw_gradebook):

    gradebook_new = []
    highest = 0

    # assignment grade, dropping the lowest 
    for student in raw_gradebook : 
        lowest = student[1]
        assign_total = 0 
        for i in range(1, num_assign + 1):
            assign_total += student[i]
            if student[i] < lowest:
                lowest = student[i]

        s_total = assign_total - lowest + student[-1]
        gradebook_new.append([student[0],s_total])

        if s_total > highest:
            highest = s_total

    for student in gradebook_new:
        student.append(math.ceil(student[1]/highest *100))

    for student in gradebook_new:
        s_adj = student[2]
        if s_adj >= 90:
            student.append("A")
        elif s_adj >= 80:
            student.append("B")
        elif s_adj >= 70:
            student.append("C")
        elif s_adj >= 60:
            student.append("D")
        else: 
            student.append("F")
    
    return gradebook_new

num_stu, num_assign = map(int, input().split())

raw_gradebook  = []

for _ in range(num_stu):
    raw_gradebook .append(list(input().split()))

for person in raw_gradebook : 
    for i in range(1, num_assign+2):
        person[i] = int(person[i])


result = computeGrade(num_stu, num_assign, raw_gradebook)

for row in result:
    print(" ".join(map(str, row)))