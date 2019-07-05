class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __del__(self):
        print(self.__class__.__name__+" Object died")

if __name__ == '__main__':
    p1 = Point()
    p2 = p1
    p3 = p1
    print(id(p1),id(p2),id(p3))
    del p1
    del p2
    del p3
    
