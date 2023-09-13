def count_first_letter(name):
    first_letter = name[0]  # Get the first letter of the name
    count = 0  # Initialize a counter

    for letter in name:
        if letter == first_letter:
            count += 1  # Increment the counter if the letter matches the first letter

    return count

# Read input
name = input()

# Calculate and print the result
result = count_first_letter(name)
print(result)