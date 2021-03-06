#!/usr/bin/python3
""" 7-rectangle.py: Defines rectangle based on 2-rectangle.py
"""


class Rectangle:
    """ Define Class with validated private instance
        attributes width and height

        Attributes:
            number_of_instances: number of instances of rectangle
            print_symbol: public class attribute
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initializes rectangle size

            Args:
            width: width of rectangle
            height: height of rectangle
        """

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns a string of Rectangle instance using # or empty string"""

        if self.width == 0 or self.height == 0:
            return ""
        x = "{}".format(self.print_symbol) * self.width
        rect = x
        for i in range(self.height - 1):
            rect += "\n" + x
        return rect

    def __repr__(self):
        """
            Returns a string representation
            able to create new instance
        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
            Print 'Bye rectangle ...' when the instances is deleted
        """
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @property
    def width(self):
        """Defines width of the rectangle and returns its value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Defines the value of width of rectangle and checks if >= 0"""

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Defines height of the rectangle and returns its value"""

        return self.__height

    @height.setter
    def height(self, value):
        """Defines the value of height of rectangle and checks if >= 0"""

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Return area of the rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle"""
        if self.width and self.height == 0:
            return 0
        return (self.width + self.height) * 2
