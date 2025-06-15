import math

def main():
    while(True):
        try:
            a = float(input("Enter a (non-zero): "))
            b = float(input("Enter b: "))
            c = float(input("Enter c: "))
            
            if a == 0:
                print("Error: 'a' cannot be zero in a quadratic equation.")
                return

            discriminant = b ** 2 - 4 * a * c

            if discriminant < 0:
                print("There are no real roots.")
                
            elif discriminant == 0:
                root = -b / (2 * a)
                print("There is one real root:", root)

            else:
                root1 = (-b + math.sqrt(discriminant)) / (2 * a)
                root2 = (-b - math.sqrt(discriminant)) / (2 * a)
                print("There are two real roots:")
                print("Root 1:", root1)
                print("Root 2:", root2)

        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

        except ValueError:
            print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
