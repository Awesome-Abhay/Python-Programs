import os
os.system("cls")
name=["ram", "shyam", "radhika","radha","murli"]
for student in name:
    if student=="radha":
        break; #--> semicolon is optional
    print(student, end=" ")
print("")

for item in name:
    if item=="radhika":
        continue
    print(item, end=" ")