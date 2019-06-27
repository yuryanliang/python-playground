from abc import ABCMeta, abstractmethod



class Rectangle:
    __metaclass__=ABCMeta

    def __init__(self, length, width):
        self.length=length
        self.width=width
    @abstractmethod
    def area(self):
        return self.length*self.width
class Square(Rectangle):
    # def __init__(self, length):
        # super().__init__(length,length)
        pass
# class Cube(Square):
#     def surface_area(self):
#         return super().area()*6
if __name__=='__main__':
    r=Rectangle(1,1)

    s=Square(4,4)
    print(s.area())
    # t=Cube(3)
    # print(t.surface_area())