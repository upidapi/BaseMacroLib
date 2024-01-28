""" abstract represantation for a mouse """


from abc import ABC, abstractmethod


class Mouse(ABC):
    """ abstract represantation for a mouse """

    @staticmethod
    @abstractmethod
    def get_position():
        """ gets the current x,y pos of the mouse """

    @staticmethod
    @abstractmethod
    def move_to(x, y):
        """ move mouse to {x}, {y}"""

    @staticmethod
    @abstractmethod
    def listen(queue):
        """ 
        listens to (linux) os mouse events 
        puts these events in the event queue
        """

    @staticmethod
    @abstractmethod
    def press(button):
        """ press mouse button """

    @staticmethod
    @abstractmethod
    def release(button):
        """ release mouse button """

    @staticmethod
    @abstractmethod
    def move_relative(x, y):
        """ move mouse relative to it's current position """

    @staticmethod
    @abstractmethod
    def wheel(delta=1):
        """ scroll the mouse wheel {delta} determins the direction"""
