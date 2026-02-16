from datetime import date

# Get date of birth from user
year = int(input("Enter your birth year (YYYY): "))
month = int(input("Enter your birth month (MM): "))
day = int(input("Enter your birth day (DD): "))

# Today's date
today = date.today()

# Calculate age
age = today.year - year

# Check if birthday has occurred this year
if (today.month, today.day) < (month, day):
    age -= 1

print(f"You are {age} years old.")
