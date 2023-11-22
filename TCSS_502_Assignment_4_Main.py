
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self):
        self._name=""
        self._area=0
        self._perimeter=0

    @abstractmethod
    def area(self):
        return self._area

    @abstractmethod
    def perimeter(self):
        return self._perimeter

    @property
    def name(self):
        return self._name

    @property
    def draw(self):
        return self.__str__()

    def __str__(self):
        return f'{self.name}- Area: {self.area()}, Perimenter: {self.perimeter()}'

    def __eq__(self, other):
        if isinstance(other, Shape):
            return (self.name == other.name and self.area() == other.area())
        else:
            raise TypeError("You are not comparing objects of the same class!")

    def __lt__(self, other):
        if isinstance(other, Shape):
            return (self.name < other.name or (self.name==other.name and self.area() < other.area()))
        else:
            raise TypeError("You are not comparing objects of the same class!")

    def __gt__(self, other):
        if isinstance(other, Shape):
            return (self.name > other.name or (self.name==other.name and self.area() > other.area()))
        else:
            raise TypeError("You are not comparing objects of the same class!")

class Circle(Shape):
    def __init__(self,radius=0):
        self._name="Circle"
        self._radius=radius
    def area(self):
        return 3.14159*self._radius**2
    def perimeter(self):
        return 3.14159*2*self._radius

class Square(Shape):
    def __init__(self,length=0):
        self._name="Square"
        self._length=length
    def area(self):
        return self._length**2
    def perimeter(self):
        return 4*self._length

class Rectangle(Shape):
    def __init__(self,length=0,width=0):
        self._name="Rectangle"
        self._length=length
        self._width=width
    def area(self):
        return self._length*self._width
    def perimeter(self):
        return 2*self._length+2*self._width

class Triangle(Shape):  #assume all triangles are isosceles triangles
    def __init__(self,base=0,height=0):
        self._name="Triangle"
        self._base=base
        self._height=height
    def area(self):
        return .5*self._base*self._height
    def perimeter(self):
        return math.sqrt(4*self._height**2+self._base**2+self._base)


class ShapeFactory(ABC):
    @abstractmethod
    def create_shape(shape_type,*args):
        if shape_type=="Circle":
            R=Circle(args[0])
        elif shape_type=="Square":
            R=Square(args[0])
        elif shape_type=="Rectangle":
            R=Rectangle(args[0],args[1])
        elif shape_type=="Triangle":
            R=Triangle(args[0],args[1])
        else:
            raise ValueError("Shape not recognized.")
        return R

class DrawingProgramIterator:
    def __init__(self,shape_list):
        self._shape_list=shape_list
        self._index=0

    def __next__(self):
        if self._index == len(self._shape_list):
            raise StopIteration()

        temp_shape=self._shape_list[self._index]
        self._index+=1
        return temp_shape

    def __iter__(self):
        return self


class DrawingProgram:
    def __init__(self,shape_list=[]):
        self._shape_list=shape_list

    def __iter__(self):
        return DrawingProgramIterator(self._shape_list)

    def add_shape(self,shape):
        self._shape_list.append(shape)

    def remove_shape(self,shape_to_remove):
        num_shapes_removed=0
        keep_shape_list=[]
        for shape in self._shape_list:
            if shape!=shape_to_remove:
                keep_shape_list.append(shape)
            else:
                num_shapes_removed+=1
        self._shape_list=keep_shape_list
        return num_shapes_removed

    def print_shape(self,shape_to_print):
        for shape in self._shape_list:
            if shape==shape_to_print:
                print(shape)


    def sort_shapes(self):
        self._shape_list=merge_sort(self._shape_list)


    def __str__(self):
        shape_list_string=""
        for shape in self._shape_list:
            shape_list_string=shape_list_string+shape.draw+'\n'
        return shape_list_string

    def get_shape(self,index):
        if len(self._shape_list)>0 and index<=len(self._shape_list)-1:
            return self._shape_list[index]
        else:
            raise ValueError("Nah homey. Your index is wrong.")

    def set_shape(self,index,shape):
        if len(self._shape_list)>0 and index<=len(self._shape_list)-1:
            self._shape_list[index]=shape
            return self._shape_list[index]
        else:
            raise ValueError("Nah homey. Your index is wrong.")

    def clear_all_shapes(self):
        self._shape_list=[]

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid= len(list)//2
    left=list[:mid]
    right = list[mid:]
    return merge(merge_sort(left),merge_sort(right))

def merge(left, right):
    result = []
    i=j=0
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

class DrawingProgramMain(ABC):
    @abstractmethod
    def do_stuff():
        d=DrawingProgram()
        c = ShapeFactory.create_shape("Circle", 1)
        s = ShapeFactory.create_shape("Square", 9)
        r = ShapeFactory.create_shape("Rectangle", 2, 2)
        r2 = ShapeFactory.create_shape("Rectangle", 2, 2)
        t = ShapeFactory.create_shape("Triangle", 1, 4)
        d.add_shape(c)
        d.add_shape(s)
        d.add_shape(r)
        d.add_shape(r2)
        d.add_shape(t)
        print("These shapes are in the drawing program:")
        for shape in d:
            print(shape)
        print("")
        print("We will remove the rectangles.")
        print("")
        print("Total number of rectangles deleted from the list: ", d.remove_shape(r))
        print("")
        print("These are the shapes remaining in the list:")
        print("")
        print(d)
        print("")
        print("We will remove all shapes.")
        d.clear_all_shapes()
        print("")
        print("These are the shapes remaining in the list:")
        print("")
        print(d)
        print("")
        print("We will attempt to sort with no shapes in the list:")
        d.sort_shapes()
        print("")
        print(d)
        print("")
        print("Now we add one shape, sort, and print.")
        print("")
        d.add_shape(c)
        d.sort_shapes()
        print("")
        print(d)
        print("")
        print("Now we add lots of shapes and sort.")
        print("")
        c = ShapeFactory.create_shape("Circle", 1)
        s = ShapeFactory.create_shape("Square", 9)
        r = ShapeFactory.create_shape("Rectangle", 2, 2)
        t = ShapeFactory.create_shape("Triangle", 1, 4)
        c1 = ShapeFactory.create_shape("Circle", .5)
        s1 = ShapeFactory.create_shape("Square", 1)
        r1 = ShapeFactory.create_shape("Rectangle", 1, 3)
        t1 = ShapeFactory.create_shape("Triangle", .5, .5)
        d.add_shape(c)
        d.add_shape(s)
        d.add_shape(r)
        d.add_shape(t)
        d.add_shape(c1)
        d.add_shape(s1)
        d.add_shape(r1)
        d.add_shape(t1)
        print("")
        d.sort_shapes()
        print("")
        print(d)
        print("")
        print("Testing the get_shape(index) method. Take index 3, the fourth shape above:")
        print(d.get_shape(3))
        print("")
        print("Testing the set_shape(index,shape) method:")
        print("You will replace this shape at index 3 with a cirlce of no radius: ", '\n', d.get_shape(3))
        print("")
        replacement_shape = ShapeFactory.create_shape("Circle", 0)
        print("The new shape at index 3 is...")
        print(d.set_shape(3, replacement_shape))
        print("")
        print(d)







DrawingProgramMain.do_stuff()
c=Circle(1)
print(c.draw)
s=Square(4)
print(s.draw)
r=Rectangle(4,4)
print(r.draw)
t=Triangle(4,4)
print(t.draw)
print("")
print("Circle = Square :",c==s)
print("Circle > Square :",c>s)
print("Circle < Square :",c<s)
print("Rectangle = Triangle", r==t)
print("")
