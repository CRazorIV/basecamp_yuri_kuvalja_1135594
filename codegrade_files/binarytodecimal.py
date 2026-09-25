def binary_to_decimal(binary: str) -> int:
    decimal = 0

    for digit in binary:
        decimal = decimal * 2 + int(digit)

    return decimal

binary = input("Binary: ")

print(f"{binary_to_decimal(binary)}")
