import sys


def trailing() -> None:
    # argv[0] is the name of the program
    for i in range(1, len(sys.argv)):
        print("working on", sys.argv[i])
        trailing_from_file(sys.argv[i])


def trailing_from_file(filename: str) -> None:
    lines: list[str]

    with open(filename, "r") as trail_file:
        lines = trail_file.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].rstrip()

    with open(filename, "w") as trail_file:
        for line in lines:
            trail_file.write(line + "\n")
