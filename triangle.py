

'''Made by Topi Aila'''

def triangleCheck(a,b,c):
    triangletype = ""
    if (a == b and b == c and c == a):    
        triangletype = "equilateral"
        return triangletype

    elif(a == b or a == c or b == c):
        triangletype = "isosceles"
        return triangletype

    elif(a != b and b != c):
        triangletype = "irregular"
        return triangletype

