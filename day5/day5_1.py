# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

# 🚨 Don't change the code above 👆


#Write your code below this row 👇

print(student_heights)

counts = 0
for count in student_heights:
    counts +=count
    
print(counts)
average = counts/len(student_heights)
print(round(average))