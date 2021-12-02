depths = [int(line.rstrip("\n")) for line in open("input")]

previous_sum = None
number_of_depth_increases = 0
for i in range(len(depths)):
    current_sum = sum(depths[i:i+3])

    if previous_sum is not None and current_sum > previous_sum:
        number_of_depth_increases += 1

    previous_sum = current_sum

print(number_of_depth_increases)