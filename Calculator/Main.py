import os
import matplotlib.pyplot as plt
from Formulas import *
while True:
    os.system('cls')
    if input("Would you like to use a Formula(1) or Graph(2)\n") == '1':
        os.system('cls')
        ans = input(("What formula would you like to use?\n"
                     "Quadratic(1)\n"
                     "Radians to Degrees(2)\n"
                     "Degrees to Radians(3)\n"
                     "Law of cosines(4)\n"
                     "Law of Sines(5)\n"))
        os.system('cls')
        match ans:
            case '1':
                a = float(input("What is the value of a?"))
                b = float(input("what is the value of b?"))
                c = float(input("what is the value of c?"))
                print(quadratic(a,b,c))
            case '2':
                print(rad_to_deg())
            case '3':
                print(deg_to_rad())
            case '4':
                print(law_of_cosines())
            case '5':
                print(law_of_sines())
    else:
        os.system('cls')
        x,y = [],[]
        ans = input(("What type of graphing would you like to do?\n"
                     "Slope-intercept (y = mx + b)(1)\n"
                     "Exponential Growth/Decay (y = ab^x)(2)\n"
                     "Quadratic (y = ax^2 + bx + c)(3)\n"))
        os.system('cls')
        match ans:
            case '1':
                print("y = mx + b")
                xy = slope_intercept()
                x,y = xy[0],xy[1]
            case '2':
                print("y = ab^x")
                xy = exponential_graph()
                x,y = xy[0],xy[1]
            case '3':
                print("y = ax^2 + bx + c")
                xy = quadratic_graph()
                x,y = xy[0],xy[1]
        plt.plot(x,y)
        plt.grid()
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')
        plt.show()
    if input("Would you like to restart?(y/n)") != 'y': break
os.system('cls')