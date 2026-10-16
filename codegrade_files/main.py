import os, sys

valid_lines = []
corrupt_lines = []

def read_csv_as_string_list(filepath: str) -> list:
    """
    Reads a CSV file and returns a list of strings,
    each representing a row (excluding the first row which is the header).
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    cleaned_lines = []
    for line in lines[1:]:
        cleaned_line = line.strip()
        cleaned_lines.append(cleaned_line)
    return cleaned_lines

def is_valid_postcode(postcode: str) -> bool:
    """
    Validates Dutch postcode format using basic loops and string checks.
    Format: 4 digits followed by 2 uppercase letters (optional space allowed).
    """
    postcode = postcode.replace(" ", "")
    if len(postcode) != 6:
        return False
    for i in range(4):
        if not postcode[i].isdigit():
            return False
    for i in range(4, 6):
        if not postcode[i].isalpha():
            return False
    return True

def is_valid_name(name: str) -> bool:
    if name == "":
        return False
    for c in name:
        if not c.isalpha() and c != " ":
            return False
    return True

def is_positive(value: str) -> bool:
    """
    Checks if the value is a positive non-zero float.
    """
    try:
        num = float(value)
        return num > 0
    except (ValueError, TypeError):
        return False


def filter_data(rows: list) -> None:
    """
    Processes the rows extracted from the input file, checks all the requested validity conditions 
    and fills valid_lines and corrupt_lines.
    """
    for row in rows:
        fields = row.split(",")
        if len(fields) != 11:
            corrupt_lines.append((row, "Invalid row length"))
            continue

        sender_first = fields[0]
        sender_last = fields[1]
        receiver_first = fields[2]
        receiver_last = fields[3]
        weight = fields[4]
        length = fields[5]
        width = fields[6]
        height = fields[7]
        street = fields[8]
        house_number = fields[9]
        postcode = fields[10]

        errors = []

        if not is_valid_name(sender_first) or not is_valid_name(sender_last):
            errors.append("Invalid sender name")
        if not is_valid_name(receiver_first) or not is_valid_name(receiver_last):
            errors.append("Invalid receiver name")
        if not is_positive(weight):
            errors.append("Invalid weight")
        if not is_positive(length) or not is_positive(width) or not is_positive(height):
            errors.append("Invalid box dimensions")
        if street == "":
            errors.append("Invalid street")
        if house_number == "":
            errors.append("Invalid house number")
        if not is_valid_postcode(postcode):
            errors.append("Invalid postcode")

        if errors:
            corrupt_lines.append((row, ", ".join(errors)))
        else:
            valid_lines.append(row)

def organise_packages_by_postcode(valid_rows)->None:
    """
    For each valid package row:
    - Calculates volume: Length * Width * Height
    - Creates a tuple: (postcode, street + house number, volume)
    - Prints all triples for reporting
    """
    package_groups = []

    for row in valid_rows:
        fields = row.split(",")
        postcode = fields[10].replace(" ", "")
        street = fields[8]
        house_number = fields[9]
        length = float(fields[5])
        width = float(fields[6])
        height = float(fields[7])
        volume = round(length * width * height, 2)
        package_groups.append((postcode, street + " " + house_number, volume))

    print("### VALID LINES ###")
    for row in valid_rows:
        print(row)

    print()
    print("### ORGANISED PACKAGES BY POSTCODE ###")
    for postcode, address, volume in package_groups:
        print(f"Postcode: {postcode}, Address: {address}, Volume: {volume}")

def report_corrupt_data()->None:
    """
    Prints all corrupt rows with their issues.
    """
    print()
    print("### CORRUPT LINES ###")
    for row, errors in corrupt_lines:
        print(f"{row}  -->  {errors}")


def main():
    # Define the file path relative to the script
    filename = "packages.csv"  # Replace with your actual CSV filename
    # Step 1: Read and clean the data
    rows = read_csv_as_string_list(filename)
    # Step 2: Polish and validate the data
    filter_data(rows)
    # Step 3: Report valid lines and group packages
    organise_packages_by_postcode(valid_lines)
    # Step 4: Report corrupt lines
    report_corrupt_data()

if __name__ == "__main__":
    main()