class Circle:
    """A simple class representing a circle.

    This class allow users to create instance of class Circle and get area.

    Attributes:
        - radius (int): radius of the circle

    Class variable:
        - PI (float): constant with value 3.14

    Class methods:
        - from_diameter(diameter): create inctance of class Circle with given diameter

    Static methods:
        - check_radius(radius): check if radius is greater than 0

    Methods:
        - __init__(radius): Initializes the circle with the given radius
        - get_area(): Returns the area of circle
        - __str__(): Returns the string representation of instance

    Example usage:
    >>> circle = Circle(10)
    >>> area = circle.get_area()
    >>> circle_from_diameter = Circle.from_diameter(10)
    >>> area_from_diameter = circle_from_diameter.get_area()
    >>> print(area)
    314.0
    >>> print(circle_from_diameter)
    Circle with radius 5.0
    >>> print(area_from_diameter)
    78.5
    """
    PI = 3.14

    def __init__(self, radius):
        """Initializes the circle with the given radius

        Raises:
            ValueError: Radius must be greater than 0
        """
        if not self.check_radius(radius):
            raise ValueError("Radius must be greater than 0")

        self.radius = radius

    def get_area(self):
        """Returns the area of circle"""
        return self.PI * (self.radius ** 2)

    @classmethod
    def from_diameter(cls, diameter):
        """Returns the instance of the class Circle with radius, get from the diameter

        Raises:
            - ValueError if diameter is less than 0
        """
        radius = diameter / 2

        if not cls.check_radius(radius):
            raise ValueError("Radius must be greater than 0")

        return Circle(diameter / 2)

    @staticmethod
    def check_radius(radius):
        """Checks if the radius is greater than 0"""
        return radius > 0

    def __str__(self):
        """Returns a string representation of instance"""
        return f"Circle with radius {self.radius}"


circle_1 = Circle(10)
area_1 = circle_1.get_area()

circle_2 = Circle.from_diameter(10)
area_2 = circle_2.get_area()

print(area_1)
print(area_2)
