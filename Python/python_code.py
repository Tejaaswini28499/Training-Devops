weekly_expenses = 1000
total_expenses = 0


for i in range(52):
    total_expenses = total_expenses + weekly_expenses
    print(i+1, "week expenses =", total_expenses)
print("total expenses for this month is", total_expenses )
