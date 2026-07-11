from employees import employees
from attendance import attendance
from payroll import compute_pay

employee = employees[0]
record = attendance[0]

result = compute_pay(employee, record)

print("===== PAYSLIP =====")
print("Employee ID:", employee["id"])
print("Name:", employee["name"])
print("Position:", employee["position"])
print("Gross Pay:", result["gross_pay"])
print("Overtime Pay:", result["overtime_pay"])
print("Total Pay:", result["total_pay"])
print("Deductions:", result["total_deductions"])
print("Net Pay:", result["net_pay"])
print("===================")
