import math

def scientific_calculator():
    while True:
        print("\n--- Scientific Calculator ---")
        print("--- Developed By Nahid-B09 ---\n")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Power (a^b)")
        print("6. Square Root")
        print("7. Logarithm (base 10)")
        print("8. Natural Log (ln)")
        print("9. Sine")
        print("10.Cosine")
        print("11.Tangent")
        print("12.Factorial")
        print("13.PI(π)")
        print("0. Exit")

        choice = input("Select an option: ")

        try:
            if choice == "1":
                a, b =10,20
                print(f"Addition of {a} and {b} is {a + b}")

            elif choice == "2":
                a, b = 10,20
                print(f"Subtraction of {a} and {b} is {a - b}")

            elif choice == "3":
                a, b = 10,20
                print(f"Multiplication of {a} and {b} is {a * b}")

            elif choice == "4":
                a, b =20,10
                print(f"Division of {a} and {b} is {a / b}")

            elif choice == "5":
                a, b = 10,5
                print(f"Power of {a} ^ {b} is {math.pow(a, b)}")


            elif choice == "6":
                x = 25
                print(f"Sqrt({x})={math.sqrt(x)}")

            elif choice == "7":
                x =100
                print(f"logarithm {x} is {math.log10(x)}")

            elif choice == "8":
                x = 100
                print(f" Natural logarithm {x} is {math.log(x)}")

            elif choice == "9":
                x = 30
                print(f"Sin({x}) : {math.sin(math.radians(x))}")

            elif choice == "10":
                x = 30
                print(f"cos({x}) :{math.cos(math.radians(x))}")

            elif choice == "11":
                x = 30
                print(f"tan({x}) : {math.tan(math.radians(x))}")

            elif choice == "12":
                x =5
                print(f"Factorial of {x} is {math.factorial(x)}")
            elif choice == "13":
            
                print(f"PI(π) = {math.pi}")

            elif choice == "0":
                print("Calculator closed.")
                break

            else:
                print("Invalid choice!")

        except Exception as e:
            print("Error:", e)

# Run calculator
scientific_calculator()
