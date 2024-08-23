'''
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out
'''
monthly_expenses = [2200, 2350, 2600, 2130, 2190]


# 1. In Feb, how many dollars you spent extra compare to January
extra_money = monthly_expenses[1] - monthly_expenses[0]
print("1. In Feb, how many dollars you spent extra compare to January: ", extra_money)

# 2. Find out your total expense in first quarter (first three months) of the year.
first_quarter_total_expense = monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2]
print("2. Total expense in first quarter (first three months) of the year: ", first_quarter_total_expense)

# 3. Find out if you spent exactly 2000 dollars in any month
def findout(list):
    for amount in monthly_expenses:
        if amount == 2000:
            return True
        else:
            continue
    return False

if findout(monthly_expenses):
    print("3. You spent exactly 2000 in at least 1 month")
else:
    print("3. You didn't spend exactly 2000 in any month")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
monthly_expenses.append(1980)
print("4. Adjusted monthly expense list: ", monthly_expenses)

'''
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''
monthly_expenses[3] = monthly_expenses[3] + 200
print("5. Corrected monthly expense list: ", monthly_expenses)