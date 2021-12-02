position, aim = [0, 0], 0 # [horiz, depth], aim
for [action, amount] in [line.rstrip("\n").split(" ") for line in open("input")]:
    position = [position[0] + int(amount), position[1] + (int(amount) * aim)] if action == "forward" else position
    aim += int(amount) if action == "down" else (- int(amount)) if action == "up" else 0

print(position[0] * position[1])