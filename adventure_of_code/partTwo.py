from help_functions import get_data
line_without_newline = get_data()

group_of_three = []

for i in range(0,len(line_without_newline)):
    group_of_three.append(line_without_newline[i:i+3])

group_sum_numbers = []

for group in group_of_three:
    convert_to_numebers = list(map(int, group))
    total_number = sum(convert_to_numebers)
    group_sum_numbers.append(total_number)

larger_measurements = 0
active_value = group_sum_numbers[0]

for line in group_sum_numbers:
    if line > active_value:
        larger_measurements += 1
        active_value = line
    else:
        active_value = line
        
print(f"Larger measurments: {larger_measurements}")
