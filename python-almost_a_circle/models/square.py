#!/usr/bin/python3
"""this module define a class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """this define it"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width 
        )
