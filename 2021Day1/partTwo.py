with open('C:/Github/AdventOfCode/2021Day1/messureData.txt') as f:
    lines = f.readlines()
    f.close()

line_without_newline = []

for line in lines:
    line = line.rstrip("\n")
    line_without_newline.append(line)

group_of_three = [line_without_newline[i:i+3] for i in range(0, len(line_without_newline), 3)]
# Av någon anledning får man inte med alla värden i listan, det fungerar på exemplet nedan
group_sum_numbers = []

for group in group_of_three:
    convert_to_numebers = list(map(int, group))
    total_number = sum(convert_to_numebers)
    group_sum_numbers.append(total_number)

larger_measurements = 1
active_value = group_sum_numbers[0]

for line in group_sum_numbers:
    if line > active_value:
        larger_measurements += 1
        active_value = line
    else:
        active_value = line

# print(f"Larger measurments: {larger_measurements}")


# TEST NEDAN

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
group_test = [test[i:i+3] for i in range(0, len(test), 3)]
print(group_test)

sum_numbers = []

for group in group_test:
    # total_number = group[0] + group[1] + group[2]
    total_number =sum(group)
    sum_numbers.append(total_number)

print(sum_numbers)


# result = sum(test[:3])
# print(result)