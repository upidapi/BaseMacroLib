""" abstract represantation for a keyboard """


from abc import ABC, abstractmethod


class AbsKeyboard(ABC):
    """ abstract represantation for a keyboard """

    @staticmethod
    @abstractmethod
    def init():
        """ init the controller """

    @staticmethod
    @abstractmethod
    def press(scan_code):
        """ Sends a 'down' event for the specified scan code """

    @staticmethod
    @abstractmethod
    def release(scan_code):
        """ Sends an 'up' event for the specified scan code """

    @staticmethod
    @abstractmethod
    def map_name(name):
        """ 
        Returns a tuple of (scan_code, modifiers) where ``scan_code`` is a numeric scan code 
        and ``modifiers`` is an array of string modifier names (like 'shift') 
        """

    @staticmethod
    @abstractmethod
    def name_from_scancode(scan_code):
        """ Returns the name or character associated with the specified key code """

    @staticmethod
    @abstractmethod
    def listen(callback):
        """ starts listening to keyboard events """
 
    @staticmethod
    @abstractmethod
    def type_unicode(character):
        """ types a unicode char """
