import math
import os

def circle_area(radius):
    return math.pi * radius ** 2

def rectangle_area(length, width):
    return length * width

def square_area(side):
    return side ** 2

def triangle_area(base, height):
    return 0.5 * base * height

def triangle_area_sides(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def parallelogram_area(base, height):
    return base * height

def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def rhombus_area(diagonal1, diagonal2):
    return 0.5 * diagonal1 * diagonal2

def ellipse_area(semi_major, semi_minor):
    return math.pi * semi_major * semi_minor

def pentagon_area(side):
    return (1/4) * math.sqrt(25 + 10 * math.sqrt(5)) * side ** 2

def hexagon_area(side):
    return (3 * math.sqrt(3) / 2) * side ** 2

def sector_area(radius, angle_degrees):
    return (angle_degrees / 360) * math.pi * radius ** 2

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def continue_or_exit():
    while True:
        choice = input("\nWould you like to try again? (y/n): ").lower()
        if choice == 'y' or choice == 'yes':
            clear_screen()
            print("Area Calculator")
            print("=" * 30)
            return True
        elif choice == 'n' or choice == 'no':
            print("Thank you for using Area Calculator!")
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

def main():
    print("Area Calculator")
    print("=" * 30)
    
    while True:
        print("\nChoose a shape:")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Square")
        print("4. Triangle (base and height)")
        print("5. Triangle (three sides)")
        print("6. Parallelogram")
        print("7. Trapezoid")
        print("8. Rhombus")
        print("9. Ellipse")
        print("10. Pentagon")
        print("11. Hexagon")
        print("12. Sector")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-12): ")
        
        if choice == "0":
            print("Thank you for using Area Calculator!")
            break
        elif choice == "1":
            radius = float(input("Enter radius: "))
            area = circle_area(radius)
            print(f"Area of circle: {area:.2f}")
            if not continue_or_exit():
                break
        elif choice == "2":
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            area = rectangle_area(length, width)
            print(f"Area of rectangle: {area:.2f}")
            if not continue_or_exit():
                break
        elif choice == "3":
            side = float(input("Enter side length: "))
            area = square_area(side)
            print(f"Area of square: {area:.2f}")
            if not continue_or_exit():
                break
        elif choice == "4":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = triangle_area(base, height)
            print(f"Area of triangle: {area:.2f}")
            if not continue_or_exit():
                break
        elif choice == "5":
            a = float(input("Enter first side: "))
            b = float(input("Enter second side: "))
            c = float(input("Enter third side: "))
            area = triangle_area_sides(a, b, c)
            print(f"Area of triangle: {area:.2f}")
            if not continue_or_exit():
                break
        elif choice == "6":
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            area = parallelogram_area(base, height)
            print(f"Area of parallelogram: {area:.2f}")
            if not continue_or_exit():
                break
        elif choice == "7":
            base1 = float(input("Enter first base: "))
            base2 = float(input("Enter second base: "))
            height = float(input("Enter height: "))
            area = trapezoid_area(base1, base2, height)
            print(f"Area of trapezoid: {area:.2f}")
            if not continue_or_exit():
                break
        elif choice == "8":
            d1 = float(input("Enter first diagonal: "))
            d2 = float(input("Enter second diagonal: "))
            area = rhombus_area(d1, d2)
            print(f"Area of rhombus: {area:.2f}")
            if not continue_or_exit():
                break
        elif choice == "9":
            semi_major = float(input("Enter semi-major axis: "))
            semi_minor = float(input("Enter semi-minor axis: "))
            area = ellipse_area(semi_major, semi_minor)
            print(f"Area of ellipse: {area:.2f}")
            if not continue_or_exit():
                break
        elif choice == "10":
            side = float(input("Enter side length: "))
            area = pentagon_area(side)
            print(f"Area of pentagon: {area:.2f}")
            if not continue_or_exit():
                break
        elif choice == "11":
            side = float(input("Enter side length: "))
            area = hexagon_area(side)
            print(f"Area of hexagon: {area:.2f}")
            if not continue_or_exit():
                break
        elif choice == "12":
            radius = float(input("Enter radius: "))
            angle = float(input("Enter angle in degrees: "))
            area = sector_area(radius, angle)
            print(f"Area of sector: {area:.2f}")
            if not continue_or_exit():
                break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
