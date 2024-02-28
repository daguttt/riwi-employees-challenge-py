from json import load
from random import randrange

# 1.
with open('employees.json', 'r') as employees_file:
    employees = load(employees_file)

# print(len(employees)) # 13
# 2.
random_employee_index = randrange(0, len(employees))
selected_employee = employees[random_employee_index]

# 3.
employee_years_of_service = selected_employee["years_of_service"]
salary_increment = 0
if employee_years_of_service > 3:
    salary_increment = 50
elif employee_years_of_service == 3:
    salary_increment = 30
elif employee_years_of_service == 2:
    salary_increment = 10
else:
    salary_increment = 0

# 4.
new_employee_salary = selected_employee["base_salary"] * \
    (100 + salary_increment) / 100

# print(selected_employee)
# print(new_employee_salary)

# 5.
overview_template = """
--- Incremento {name}. Departamento: IT   ---

Id del usuario: {id}
Nombre: {name}
Departamento: IT
Años De Servicio: {years_of_service}
Salario Original: {base_salary} USD/YEAR
Incremento Aplicado: {salary_increment}%
Nuevo salario: {new_salary} USD/YEAR
"""
print(overview_template.format(
    name=selected_employee["name"],
    id=selected_employee["id"],
    years_of_service=selected_employee["years_of_service"],
    base_salary=selected_employee["base_salary"],
    salary_increment=salary_increment,
    new_salary=new_employee_salary,
))
print("before", selected_employee)
selected_employee["base_salary"] = new_employee_salary
print("after", selected_employee)
