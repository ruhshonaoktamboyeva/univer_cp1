
def replace_value(values, index, new_value):
    values[index] = new_value


def find_first(values, target):
    for index in range(len(values)):
        if values[index] == target:
            return index
    return -1


def summarize(values):
    return min(values), max(values), sum(values)


days = int(input("Enter the number of days: "))

original = []

for i in range(days):
    practice_time = int(input("Enter typing practice time in minutes: "))
    original.append(practice_time)


updated = original[:]

index = int(input("Enter the index to correct: "))
new_value = int(input("Enter the new practice time: "))

replace_value(updated, index, new_value)


target = int(input("Enter the practice time to search for: "))

first_index = find_first(updated, target)
matching_values = updated.count(target)

minimum, maximum, total = summarize(updated)

sorted_values = sorted(updated)


print(f"Original: {original}")
print(f"Updated: {updated}")
print(f"Sorted: {sorted_values}")
print(f"Minimum practice time: {minimum} minutes")
print(f"Maximum practice time: {maximum} minutes")
print(f"Total practice time: {total} minutes")

if first_index == -1:
    print("Target not found")
else:
    print(f"First matching index: {first_index}")

print(f"Matching values: {matching_values}")

