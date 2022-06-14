employee_salaries = {
    "guido": 10000,
    "james": 20000,
    "brandon": 30000
}

extra_employee_salaries = {
    "yuki": 200000,
    "guido": 333333
}

employee_salaries.update(extra_employee_salaries)
print(employee_salaries)

extra_employee_salaries.update(employee_salaries)
print(extra_employee_salaries)