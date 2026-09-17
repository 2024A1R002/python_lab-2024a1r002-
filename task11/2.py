#write a python program to input marks of 10 students. store only valid marks between 0 and 100 in a list skip invalid marks
v_marks = []
for i in range(10):
    marks = int(input("enter marks"))
    if marks <0 or marks>100:
        continue
    v_marks.append(marks)
print(v_marks)    

        