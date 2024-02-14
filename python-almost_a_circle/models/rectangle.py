#!/usr/bin/python3
"""this module define a class Rectangle inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """this define a class constructor"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
