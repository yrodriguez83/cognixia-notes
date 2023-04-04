user_input = int(input("Enter an integer: "))
result_list = []
fizzbuzz_counts = {"Fizz": 0, "Buzz": 0, "FizzBuzz": 0, "Sum": 0}

for i in range(1, user_input + 1):
    if i % 3 == 0 and i % 5 == 0:
        result_list.append("FizzBuzz")
        fizzbuzz_counts["FizzBuzz"] += 1
    elif i % 3 == 0:
        result_list.append("Fizz")
        fizzbuzz_counts["Fizz"] += 1
    elif i % 5 == 0:
        result_list.append("Buzz")
        fizzbuzz_counts["Buzz"] += 1
    else:
        result_list.append(i)
        fizzbuzz_counts["Sum"] += i

for element in result_list:
    print(element)

print(f"Sum of all integers: {fizzbuzz_counts['Sum']}")
print(f"Count of Fizz: {fizzbuzz_counts['Fizz']}")
print(f"Count of Buzz: {fizzbuzz_counts['Buzz']}")
print(f"Count of FizzBuzz: {fizzbuzz_counts['FizzBuzz']}")
