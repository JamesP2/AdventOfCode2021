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


lines = [line.rstrip("\n") for line in open(args.file)]

previous_depth = None
number_of_depth_increases = 0
for line in lines:
    current_depth = int(line)
    if previous_depth is not None and current_depth > previous_depth:
        number_of_depth_increases += 1

    previous_depth = current_depth

    vprint(line, number_of_depth_increases)

print(number_of_depth_increases)