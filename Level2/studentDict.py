student_detail = {"name":"sam", "age":20, "grade":"A", "subject":"Maths"}

for key, val in student_detail.items():
    print(f"The student's {key} is {val}")

student_detail["grade"] = "A+"
print("updated dictionary:", student_detail)

student_detail["passed"] = True
print("Newly added key-val:",student_detail)