age = input("What is your current age? ")

#According to this article by Tim Urban (Your Life in Weeks). This program tells us how many days, weeks, months we have left if we live until 90 years old.

years_remaining = 90 - int(age)

day = years_remaining * 365
week = years_remaining * 52
month = years_remaining * 12

print(f"You have {day} days, {week} weeks, and {month} months left.")
