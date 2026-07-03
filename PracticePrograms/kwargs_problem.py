employee_details = {}

def emp_details(**kwargs):
    for key, val in kwargs.items():
        print(f"Employee {key} is {val}")


emp_details(id = "e101", name="sam", dept = "HR", salary=10000, status="present")