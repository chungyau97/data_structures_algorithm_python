expenses = [2200, 2350, 2600, 2130, 2190]

spent_extra = expenses[1] - expenses[0]
print("1. In Feb, how many dollars you spent extra compare to January?\n", spent_extra)

first_quarter = expenses[0] + expenses[1] + expenses[2]
print("2. Find out your total expense in first quarter (first three months) of the year.\n", first_quarter)

exact_2000 = 2000 in expenses
print("3. Find out if you spent exactly 2000 dollars in any month\n", exact_2000)

expenses.append(1980)
print("4. June month just finished and your expense is 1980 dollar. Add this item "
      + "to our monthly expense list\n", expenses)

expenses[3] = expenses[3] - 200
print("5. You returned an item that you bought in a month of April and \ngot a refund "
      + "of 200$. Make a correction to your monthly expense list \nbased on this\n", expenses[3])