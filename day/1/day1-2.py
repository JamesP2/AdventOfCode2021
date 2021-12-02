import argparse

parser = argparse.ArgumentParser(description="Sonar Sweep Pt 2")
parser.add_argument("file", metavar="INPUT_FILE", type=str, help="Input filename")
parser.add_argument(
    "--verbose", "-v", action="store_true", default=False, help="Verbose output"
)

args = parser.parse_args()


def vprint(*x):
    if args.verbose:
        if len(x) == 1:
            print(x[0])
        else:
            print(x)


depths = [int(line.rstrip("\n")) for line in open(args.file)]

previous_sum = None
number_of_depth_increases = 0
for i in range(len(depths)):
    current_sum = sum(depths[i:i+3])
    vprint(depths[i:i+3], current_sum)

    if previous_sum is not None and current_sum > previous_sum:
        number_of_depth_increases += 1

    previous_sum = current_sum

    vprint(depths[i], number_of_depth_increases)

print(number_of_depth_increases)