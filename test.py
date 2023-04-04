""" name = input("What is your name? ")
age = input("What is your age? ")
profession = input("What is your profession? ")

print("Hello, my name is " + name + ", I am " + str(age) +
      " years old, and I work as a " + profession + ".") """

# Input: enter the employee's name and age
name = input("Please enter the employee's full name: ")
age_str = input("Please enter the employee's age: ")

# Split the name into first and last names + capitalize the first letter of each + convert the rest to lowercase
first_name = name.split()[0].capitalize()
last_name = name.split()[1].capitalize()
last_name_last_two_digits_of_birth_year = ""

# check if employee's birth year is an INT value
while True:
    birth_year_str = input("Please enter the employee's birth year (YYYY): ")
    try:
        birth_year = int(birth_year_str)
        last_name_last_two_digits_of_birth_year = str(birth_year)[-2:]
        break
    except ValueError:
        print("Please enter a valid year.")

# Convert the age to an integer
age = int(age_str)

# Generate the employee's email address
email = f"{first_name.lower()}.{last_name.lower()}{last_name_last_two_digits_of_birth_year}@company.com"

# Print all the results to the screen
print(f"Name: {first_name} {last_name}")
print(f"Age: {age}")
print(f"Birth year: {birth_year}")
print(f"Email: {email}")
