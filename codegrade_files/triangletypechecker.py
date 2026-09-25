def parse_side(part: str) -> float:
    return float(part[2:])


def classify_triangle(a: float, b: float, c: float) -> str:
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"


part_a, part_b, part_c = input("Sides: ").split(', ')

side_a: float = parse_side(part_a)
side_b: float = parse_side(part_b)
side_c: float = parse_side(part_c)

print(classify_triangle(side_a, side_b, side_c))
