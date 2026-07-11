def compute_pay(employee, record):
    gross_pay = employee["rate"] * record["days_worked"]
    overtime_pay = (
        record["overtime_hours"] *
        employee["overtime_rate"]
    )
    total_pay = gross_pay + overtime_pay

    late_deduction = 100
    loan_deduction = 500

    total_deductions = (
        late_deduction + loan_deduction
    )

    net_pay = total_pay - total_deductions

    return {
        "gross_pay": gross_pay,
        "overtime_pay": overtime_pay,
        "total_pay": total_pay,
        "total_deductions": total_deductions,
        "net_pay": net_pay
    }
