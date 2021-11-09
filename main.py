# Start
# The Main Menu
print('''
-----------------------------------------------------------------------
Welcome to Shape Area Calculation System (SACS) 
-----------------------------------------------------------------------
1. Triangle 2. Rectangle 3. Trapezoid
4. Circle    5. Ellipse       6. Parallelogram
''')
# Taking The input
choice = input('Please select the shape you would like to calculate the area for (1-6):')
# checking if it is an integer or not
try:
    x = int(choice)
    # if a valid number or not
    if (x < 7 and x > 0):
        print("Thank you!")
        c = "The shape you selected is:"
        # showing the user his/her choice
        if (x == 1):
            print(c + 'Triangle')
            b = float(input("Please input the Base (in centimeter):"))  # Asking for associated parameter
            h = float(input("Please input the Hight (in centimeter):"))  # Asking for associated parameter
            a = float(b * h) / 2  # Calculation
            print("The area of the Triangle is ", a, " square centimeters.")  # showing the area output
            print('''
      Thanks for using Shape Area Calculation System!
      Goodbye!
      ''')
        if (x == 2):
            print(c + 'Rectangle')
            b = float(input("Please input the Base (in centimeter):"))  # Asking for associated parameter
            h = float(input("Please input the Hight (in centimeter):"))  # Asking for associated parameter
            a = float(b * h)  # Calculation
            print("The area of the Rectangle is ", a, " square centimeters.")  # showing the area output
            print('''
      Thanks for using Shape Area Calculation System!
      Goodbye!
      ''')
        if (x == 3):
            print(c + 'Trapezoid')
            b1 = float(input("Please input the Base1 (in centimeter):"))  # Asking for associated parameter
            b2 = float(input("Please input the Base2 (in centimeter):"))  # Asking for associated parameter
            h = float(input("Please input the Hight (in centimeter):"))  # Asking for associated parameter
            a = float((b1 + b2) * h) / 2  # Calculation
            print("The area of the Trapezoid is ", a, " square centimeters.")  # showing the area output
            print('''
      Thanks for using Shape Area Calculation System!
      Goodbye!
      ''')
        if (x == 4):
            import math

            print(c + 'Circle')
            r = float(input("Please input the Radius (in centimeter):"))  # Asking for associated parameter
            a = float(math.pi * (math.pow(r, 2)))  # Calculation
            print("The area of the Circle is ", a, " square centimeters.")  # showing the area output
            print('''
      Thanks for using Shape Area Calculation System!
      Goodbye!
      ''')
        if (x == 5):
            print(c + 'Ellipse')
            import math

            y1 = float(input("Please input the Y axis radius (in centimeter):"))  # Asking for associated parameter
            x1 = float(input("Please input the X axis radius (in centimeter):"))  # Asking for associated parameter
            a = float(math.pi * (y1 * x1))  # Calculation
            print("The area of the Ellipse is ", a, " square centimeters.")  # showing the area output
            print('''
      Thanks for using Shape Area Calculation System!
      Goodbye!
      ''')
        if (x == 6):
            print(c + 'Parallelogram')
            b = float(input("Please input the Base (in centimeter):"))  # Asking for associated parameter
            h = float(input("Please input the Hight (in centimeter):"))  # Asking for associated parameter
            a = float(b * h)  # Calculation
            print("The area of the Parallelogram is ", a, " square centimeters.")  # showing the area output
            print('''
      Thanks for using Shape Area Calculation System!
      Goodbye!
      ''')

    # if not a valid number
    else:
        print("INVALID input!!!  Try again with a validd Number(1-6)")
# if not a integer
except ValueError:
    print("INVALID input!!!  Try again with a valid input")