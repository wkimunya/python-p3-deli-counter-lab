def line(people_in_line):
    if not people_in_line:
        print("The line is currently empty.")
    else:
        line_message = "The line is currently:"
        for index, person in enumerate(people_in_line, start=1):
            line_message += f" {index}. {person}"
        print(line_message)

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving_name = katz_deli.pop(0)
        print(f"Currently serving {serving_name}.")

# Example usage:
katz_deli = []

take_a_number(katz_deli, "Ada")  # Output: "Welcome, Ada. You are number 1 in line."
take_a_number(katz_deli, "Grace")  # Output: "Welcome, Grace. You are number 2 in line."
take_a_number(katz_deli, "Kent")  # Output: "Welcome, Kent. You are number 3 in line."

now_serving(katz_deli)  # Output: "Currently serving Ada."

take_a_number(katz_deli, "Matz")  # Output: "Welcome, Matz. You are number 3 in line."

now_serving(katz_deli)  # Output: "Currently serving Grace."
