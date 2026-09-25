def build_header(size: int) -> str:
    header = " " * 3 

    for column in range(1, size + 1):
        header += f"{column:4}"

    return header


def build_row(row: int, size: int) -> str:
    line = f"{row:3}"

    for column in range(1, size + 1):
        line += f"{row * column:4}"

    return line


def print_multiplication_table(size: int) -> None:
    print(build_header(size))

    for row in range(1, size + 1):
        print(build_row(row, size))


print_multiplication_table(10)