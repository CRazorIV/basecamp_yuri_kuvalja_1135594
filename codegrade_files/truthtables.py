def build_row(left: bool, right: bool, result: bool) -> str:
    return f"{left} + {right} = {result}"


def print_and_table() -> None:
    print("AND")

    for left in (True, False):
        for right in (True, False):
            print(build_row(left, right, left and right))


def print_or_table() -> None:
    print("OR")

    for left in (True, False):
        for right in (True, False):
            print(build_row(left, right, left or right))


print_and_table()
print()
print_or_table()
