from typing import Callable
from random import choice

from easylib.lib import split

class Generator:

    def __init__(self, length: int = 25):
        """The length specified will be the length of all things generated unless otherwise specified"""
        self.length = length

    def lorem(self, length: int = -1):
        """Will generate random lorem ipsum text"""
        text = ""
        for i in range(0, self.length if length == -1 else length):
            word = choice(loremWordList)
            text = f"{text} {word}"

    def Str(self, length: int = -1, capitalized: bool = False, special: bool = False):
        """Will generate a random string of characters"""
        chars = "qwertyuiopasdfghjklzxcvbnm"
        if capitalized:
            chars = chars.upper()
        if special:
            chars = chars + "`~!@#$%^&*()_-+={[}]|:;'<,>.?/'" + '"'
        chars = split(chars)
        text = ""
        for i in range(0, self.length if length == -1 else length):
            char = choice(chars)
            text = f"{text}{char}"
        return text

    def Int(self, length: int = -1):
        """Will generate a random number"""
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        number = ""
        for i in range(0, self.length if length == -1 else length):
            num = choice(nums)
            number = f"{number}{num}"
        return int(number)

    def Dict(self, length: int = -1, internalValueParameters: tuple = (), internalValueFunction: Callable = Str):
        """Will generate a random dictionary with sequential keys and random values"""
        Dict = {}
        for i in range(0, self.length if length == -1 else length):
            item = internalValueFunction(*internalValueParameters)
            Dict[i] = item
        return Dict

    def List(self, length: int = -1, internalItemParameters: tuple = (), internalDataFunction: Callable = Str):
        """Will generate a random list containing information specified"""
        List = []
        for i in range(0, self.length if length == -1 else length):
            item = internalDataFunction(*internalItemParameters)
            List.append(item)
        return List

    def Bool(self):
        """Will randomly return True of False"""
        return choice([False, True])

    def Type(self, special: bool = False):
        if not special:
            types = [str, int, float, list, dict, any]
        else:
            types = []
        return choice(types)

    def __int__(self):
        return self.int()

    def __str__(self):
        return self.str()
