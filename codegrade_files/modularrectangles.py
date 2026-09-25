user_width: int = int(input())
user_height: int = int(input())

def canvas() -> None:
    counter = 0 
    for row in range(user_height):
        for col in range(user_width):
            print(counter % 10, end=" ")
            counter += 1
        print()

canvas()