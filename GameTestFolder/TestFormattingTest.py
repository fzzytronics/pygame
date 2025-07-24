line_number_to_read = 5 # Example: read the 5th line (index 4)

with open('code.txt', 'r') as file:
    lines = file.readlines()
    # Access the 5th line (index 4 as lists are 0-indexed)
    specific_line = lines[0] 
    print(specific_line.strip())
    print(lines[2])