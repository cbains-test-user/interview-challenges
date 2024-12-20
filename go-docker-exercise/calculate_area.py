def calculate_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area


def main():
    print("Welcome to the Area Calculator!\n")

    radius = input("Enter the radius of the circle: ")
    area = calculate_area(radius)
    print(f"The area of the circle is: {area} square units")

    for i in range(5):
        print("Iteration number: " + i)

    numbers = [1, 2, 3, 4, 5]
    print("The 5th number is: " + numbers[5])

if __name__ = "__main__":
    main()
