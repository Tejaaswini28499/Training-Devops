weekly_expenses = 1000
total_expenses = 0


for i in range(52):
    total_expenses = total_expenses + weekly_expenses
    print(i+1, "week expenses =", total_expenses)
print("total expenses for this month is", total_expenses )


working_days = 23
salary_per_day = 10000
monthly_salary = 0

for i in range(working_days):
    monthly_salary = monthly_salary + salary_per_day
    if(i%7 == 0):
        print(i, "salary_per_day", monthly_salary)
    
print("my monthy salary is", monthly_salary)

working_days = 23
salary_per_day = 10000
monthly_salary = 0

for i in range(working_days):
    monthly_salary = monthly_salary + salary_per_day
    print(i+1, "salary_per_day", monthly_salary)
    
print("my monthy salary is", monthly_salary)
