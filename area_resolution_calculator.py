# The task is to create an area calculator for the following shapes: 
# Rectangle, Square, Triangle, Circle, Hexagon.

from math import pi, sqrt


# Explanation:
# The method __init__ is a special method used to initialize objects created from a class. 
# It stands for "initialize" and is also known as the constructor method. 
# In this case, we request two parameters: side1 and side2. These will remain as "Attributes of the Instance".       

# The function get_area() returns the shape area. In this case, it uses The formula for the area of the Rectangle,
# because is more easily implemented with another shape.

# The method __str__  returns the object representation in a string format.

# The self.__class__.__name__ is a way to get the name of the class to which an instance (object) belongs.
# If you would be working with the class Triangle, the attribute would be <Triangle>.

class Shape:
	def __init__(self, side1, side2):
		self.side1 = side1
		self.side2 = side2

	def get_area(self):
		return self.side1 * self.side2

	def __str__(self):
		return f'The area of this {self.__class__.__name__} is: {self.get_area()}'





# CLASS RECTANGLE
# We used the formula for the area of a rectangle before,
# so just create a class Rectangle that does nothing more than "inherits" from the class Shape.

class Rectangle(Shape):
	pass



# CLASS SQUARE
# We can see an excellent use of "Polymorphism" with the class Square.
# A square is just a rectangle but with all its sides equal. So we can use the same formula to get the area.
# To do that, we can edit the __init__ method, accepting just an one side as a paramenter, and passing that value to 
# the constructor of the class Rectangle.   

class Square(Rectangle):
	def __init__(self, side):
		super().__init__(side, side)



# CLASS TRIANGLE
# A triangle is half as large as the rectangle that surrounds it.
# Knowing that, we can inherit the class rectangle and modify the funtion get_area() to match with formula of the Triangle.

class Triangle(Rectangle):
	def __init__(self, base, height):
		super().__init__(base, height)
 
	def get_area(self):
		area = super().get_area()
		return area / 2

# Another use of the super() function is to call a method defined in the superclass and store the result as a variable. 



# CLASS CIRCLE 
# We define a class Circle, that uses a different constructor and methods.  
# Although Circle inherits the class Shape, you can redefine each one of the methods and attributes as you like

class Circle(Shape):
	def __init__(self, radius):
		self.radius = radius
 
	def get_area(self):
		return pi * (self.radius ** 2)



# CLASS HEXAGON 
# We only need to know the length of one of its sides to calculate its area.
# However, the formula is completely different and implies the use of square root. That's why it will use 
# the function sqrt() 

class Hexagon(Rectangle):

	def __init__(self, side):
		self.side = side
	
	def get_area(self):
		return (3 * sqrt(3) * self.side ** 2) / 2





# Results
print(Rectangle(1, 2))
print(Square(4))
print(Triangle(2, 3))
print(Circle(4))
print(Hexagon(3))
