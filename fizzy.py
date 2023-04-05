num = int(input("Enter a number: "))
counts = {"Fizz": 0, "Buzz": 0, "FizzBuzz": 0}
fizzbuzz_list = []

for i in range(1, num+1):
    if i % 3 == 0 and i % 5 == 0:
        fizzbuzz_list.append("FizzBuzz")
        counts["FizzBuzz"] += 1
    elif i % 3 == 0:
        fizzbuzz_list.append("Fizz")
        counts["Fizz"] += 1
    elif i % 5 == 0:
        fizzbuzz_list.append("Buzz")
        counts["Buzz"] += 1
    else:
        fizzbuzz_list.append(i)

print("FizzBuzz List: ", fizzbuzz_list)
print("Number of Fizz: ", counts["Fizz"])
print("Number of Buzz: ", counts["Buzz"])
print("Number of FizzBuzz: ", counts["FizzBuzz"])
# generator expression to extract only the integer elements from the fizzbuzz_list, using the isinstance() function to check if an element is an integer or not.
print("Sum of all integers: ", sum(x for x in fizzbuzz_list if isinstance(x, int)))
