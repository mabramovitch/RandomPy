import math

def quadraticformula(a, b, c):
    if (b**2 - 4*a*c) > 0:
        print "x = ", (-b + math.sqrt(b**2 - 4*a*c))/(2*a), ", ", (-b - math.sqrt(b**2 - 4*a*c))/(2*a);
    elif (b**2 - 4*a*c) == 0:
        print "x = " -b;
    else: print "No real solution, fool.";
