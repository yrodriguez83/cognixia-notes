def read_int(user_input, min_val=None, max_val=None, input_type=int):
    while True:
        try:
            value = input_type(input(user_input))
            if min_val is not None and value < min_val:
                raise ValueError(
                    f"Input must be greater than or equal to {min_val}.")
            if max_val is not None and value > max_val:
                raise ValueError(
                    f"Input must be less than or equal to {max_val}.")
            break
        except ValueError:
            print("Input must be a number. Please try again.")
    return value


# Prompt the user for an integer between 0 and 12 (inclusive).
num = read_int("Enter a number between 0 and 12: ", min_val=0, max_val=12)
