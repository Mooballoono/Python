import math
import os
def frange(x,y,inc):
    lst = []
    while x <= y:
        lst.append(x)
        x += inc
    return lst

def quadratic(a,b,c):
    x = (b**2)-(4*a*c)
    a *= 2
    if(abs(c) == 100):
        return [(-b + x**.5)/a,(-b - x**.5)/a]
    if x < 0:
        return str(-b/a) + " ± " + str(abs(x**.5)/2) + 'i'
    elif x == 0:
        return str((-b + x**.5)/a)
    else:
        return str((-b + x**.5)/a) + ' and ' + str((-b - x**.5)/a)

def rad_to_deg():
    r = input("How many radians?\n"
              "(enter the fraction or number without pi)\n"
              "(ex:for 1π/2 type 1/2)\n")
    if '/' in r:
        x = r.split('/')
        r = float(x[0])/float(x[1])
    else: r = float(r)
    return r*180  

def deg_to_rad():
    d = float(input("how many degrees?\n"))
    if d/180 != round(d/180):
        x = math.floor(d/180)
        de = 2
        nu = 1
        while (nu + de*x)/de != d/180:
            if (nu + de*x)/de > d/180:
                nu = 1
                de += 1
            else:
                nu += 1
        return str(nu + de*x) + "π/" + str(de)
    else: return str(d/180) + "π"

def law_of_cosines():
    ans = input("do you need to find a side(1) or angle(2)\n")
    if ans == '1':
        a = float(input("What is the value of side a\n")) 
        b = float(input("What is the value of side b\n"))
        C = float(input("What is the value of angle C\n"))
        return round((a**2 + b**2 - 2*a*b*math.cos(math.radians(C)))**.5,10)
    elif ans == '2':
        a = float(input("What is the value of side a\n")) 
        b = float(input("What is the value of side b\n"))
        c = float(input("What is the value of side c\n"))
        return round(math.degrees(math.acos((a**2 + b**2 - c**2)/(2*a*b))),10)
    return "thats not an answer"

def law_of_sines():
    ans = input("do you need to find a side(1) or angle(2)\n")
    if ans == '1':
        A = float(input("What is the value of angle A\n"))
        a = float(input("What is the value of side a\n"))
        B = float(input("What is the value of angle B\n"))
        return round(math.sin(math.radians(B))/(math.sin(math.radians(A))/a),10)
    elif ans == '2':
        A = float(input("What is the value of angle A\n"))
        a = float(input("What is the value of side a\n"))
        b = float(input("What is the value of side b\n"))
        return round(math.degrees(math.sin(math.radians(A))/a*b),10)
    return "thats not an answer"

def slope_intercept():
    x,y = [],[]
    m = float(input("What is the value of m?\n"))
    x1 = float(input("What is the first x value?\n"))
    x2 = float(input("What is the last x value?\n"))
    x3 = float(input("What increment would you like to increase x by?\n"))
    b = float(input("What is the value of b?\n"))
    os.system('cls')
    for i in frange(x1,x2,x3): x.append(i)
    for i in x: y.append(m*i+b)
    if b > 0: print("y = " + str(m) + "x + " + str(b))
    elif b < 0: print("y = " + str(m) + "x - " + str(b*-1))
    else:  print("y = " + str(m) + "x")
    return [x,y]

def exponential_graph():
    x,y = [],[]
    a = float(input("What is the value of a?\n"))
    b = float(input("what is the value of b? ( >= 1 for growth < 1 for decay)\n"))
    x1 = float(input("What is the first x value?\n"))
    x2 = float(input("What is the last x value?\n"))
    x3 = (x2-x1)/100
    os.system('cls')
    for i in frange(x1,x2,x3): x.append(i)
    for i in x: y.append(a*b**i)
    print("y = " + str(a) + " * " + str(b) + "^x")
    return[x,y]

def quadratic_graph():
    x,y = [],[]
    a = float(input("what is the value of a?\n"))
    b = float(input("what is the value of b?\n"))
    c = float(input("what is the value of c?\n"))
    os.system('cls')
    x1 = (b/a/2)*-1
    x2 = x1
    yt = c - x1**2*a
    print(str(x1) + "," + str(yt) + " is the vertex")
    if a*b*c > 0:
        xt = quadratic(a,b,100)
        x1,x2 = xt[0],xt[1]
    else: 
        xt = quadratic(a,b,-100)
        x1,x2 = xt[0],xt[1]
    if x1 > x2:
        x3 = (x1-x2)/100
        for i in frange(x2,x1,x3): x.append(i)
    else:
        x3 = (x2-x1)/100
        for i in frange(x1,x2,x3): x.append(i)
    for i in x: y.append(a*i**2 + b*i + c)
    return[x,y]