

class Point:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __eq__(self,other):
        return isinstance(other, Point) and \
            self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x,self.y))


p3=Point(1,2)
p4=Point(1,2)
p5=Point(3,4)
p6=Point(3,4)
p7=Point(32,44)
print(p5==p6)
print(p5==p7)
print(hash(p5))
print(hash(p6))
print(hash(p7))

r={}
r[p5]=100
print(r)
print(p3==p4)
