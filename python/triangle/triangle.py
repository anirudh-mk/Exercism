def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if 0 not in sides:
        if a==b and a==c and b==c:
            return True
        else:
            return False
    else:
        return False

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if 0 not in sides and 1 not in sides:
        if a==b or a==c or b==c:
            return True
        else:
            return False
    else:
        return False

def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    
    if 0 not in sides:
        if a!=b and a!=c and b!=c and a+b >= c and b+c >= a and a+c >= b:
            return True
        else:
            return False
    else:
        return False