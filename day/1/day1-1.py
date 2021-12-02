import argparse

parser = argparse.ArgumentParser(description="Sonar Sweep")
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


previous_depth = None
number_of_depth_increases = 0
for current_depth in [int(line.rstrip("\n")) for line in open(args.file)]:
    if previous_depth is not None and current_depth > previous_depth:
        number_of_depth_increases += 1

    previous_depth = current_depth

    vprint(current_depth, number_of_depth_increases)

print(number_of_depth_increases)