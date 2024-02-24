from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)

print(student1.on_honor_roll())
print(student2.on_honor_roll())

print(student2.gpa)

print(student1.type_of_student())
print(student2.type_of_student())
