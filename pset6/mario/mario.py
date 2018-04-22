from cs50 import get_int

while True:
    height = get_int("Height: ")
    if height <= 23 and height >= 0:
        for i in range(height):
            j = height - i - 1
            while j > 0:
                print(" ", end="")
                j = j - 1
            print("#" * (i + 1), end="  ")
            print("#" * (i + 1))
        break
