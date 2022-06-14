from help_functions import get_data
line_without_newline = get_data()

larger_measurements = 1
active_value = line_without_newline[0]
for line in line_without_newline:
    if line > active_value:
        larger_measurements += 1
        active_value = line
    else:
        active_value = line
    

print(line_without_newline)
print(f"Larger measurments: {larger_measurements}")

    
    