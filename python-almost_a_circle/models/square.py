#!/usr/bin/python3
"""this module define a class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """this define it"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    def update(self, *args, **kwargs):
        """that assigns an argument to each attribute"""
        arg_names = ["id", "size", "x", "y"]
        if args:
            for i, value in enumerate(args):
                setattr(self, arg_names[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
