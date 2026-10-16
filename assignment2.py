def classify(value):
    if value < 198:
        return "Below range"
    elif value <= 202:
        return "In range"
    else:
        return "Above range"


def calculate_average(total, count):
    return total / count


number_of_strips = int(input("Enter the number of strips: "))

total_length = 0
below_range = 0
in_range = 0
above_range = 0

for i in range(number_of_strips):
    length = int(input("Enter the strip length: "))

    classification = classify(length)
    print(classification)

    total_length += length

    if classification == "Below range":
        below_range += 1
    elif classification == "In range":
        in_range += 1
    else:
        above_range += 1

average_length = calculate_average(total_length, number_of_strips)

print(f"Total length: {total_length} mm")
print(f"Average length: {average_length} mm")
print(f"Below range: {below_range}")
print(f"In range: {in_range}")
print(f"Above range: {above_range}")