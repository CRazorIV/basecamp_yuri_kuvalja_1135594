PATTERNS = [
    "XX-99-99",
    "99-99-XX",
    "99-XX-99",
    "XX-99-XX",
    "XX-XX-99",
    "99-XX-XX",
    "99-XXX-9",
    "9-XXX-99",
    "XX-999-X",
    "X-999-XX",
    "XXX-99-X",
    "9-XX-999",
]


def matches_pattern(plate, pattern):
    # Check plate against one template, position by position.
    if len(plate) != len(pattern):
        return False

    # match each character from the plate against the one form the pattern
    for plate_char, pattern_char in zip(plate, pattern):
        if pattern_char == "X" and not (plate_char.isalpha() and plate_char.isupper()):
            return False
        if pattern_char == "9" and not plate_char.isdigit():
            return False
        if pattern_char == "-" and plate_char != "-":
            return False

    return True


def is_valid(plate):
    # A plate is valid if it matches at least one of the patterns.
    for pattern in PATTERNS:
        if matches_pattern(plate, pattern):
            return True
    return False


plate = input("License: ").strip()
print("Valid" if is_valid(plate) else "Invalid")