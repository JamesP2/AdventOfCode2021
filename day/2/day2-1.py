position = [0, 0] # [horiz, depth]
for [action, amount] in [line.rstrip("\n").split(" ") for line in open("input")]:
    position[0] += int(amount) if action == "forward" else 0
    position[1] += int(amount) if action == "down" else (- int(amount)) if action == "up" else 0

print(position[0] * position[1])