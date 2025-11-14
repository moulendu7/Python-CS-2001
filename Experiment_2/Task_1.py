age_input = input("Enter your age: ")
if not age_input.isdigit():
    print("Invalid input! Please enter a numeric value.")
else:
    age = int(age_input)
    if age < 18:
        print("You are a minor.")
    elif age <= 65:
        print("You are an adult.")
    else:
        print("You are a senior.")