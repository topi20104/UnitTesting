from unittest.main import main

'''Made by Topi Aila'''

def TriangleCheck(a,b,c):
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
        
        
print(TriangleCheck(1,2,3))