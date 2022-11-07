from typing import Callable
from random import choice
from easylib.lib import split


class Generator:

    def __init__(self, length: int = 25, nums: list = None):
        """The length specified will be the length of all things generated unless otherwise specified"""
        self.length = length
        self.nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] if nums is None else nums

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
        nums = self.nums
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

    def List(self, length: int = -1, internalItemParameters: list = [], internalDataFunction: Callable = "Default"):
        """Will generate a random list containing information specified"""
        List = []
        if internalDataFunction == "Default":
            for i in range(0, self.length if length == -1 else length):
                item = self.Str(*internalItemParameters)
                List.append(item)
        else:
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
            types = [str, int, float, list, dict, any, bool, tuple]
        return choice(types)

    def Tuple(self, length: int = -1, internalItemParameters: tuple = (), internalDataFunction: Callable = Str):
        return tuple(self.List(length=length, internalItemParameters=internalItemParameters,
                               internalDataFunction=internalDataFunction))

    def Float(self, length: int = -1):
        """Makes a random float where the 20% of the length is used to make the front of the decimal and then the
        rest is used to make the rest behind the decimal."""
        nums = self.nums
        if length == -1:
            length = self.length
        frontDecimal = round(length * .20)
        valFrontDecimal = ""
        for i in range(0, frontDecimal):
            valFrontDecimal = valFrontDecimal + str(choice(nums))
        valBackDecimal = ""
        for x in range(0, length - frontDecimal):
            valBackDecimal = valBackDecimal + str(choice(nums))
        num = f"{valFrontDecimal}.{valBackDecimal}"
        return float(num)

    def Random(self):
        function = choice([self.Int, self.Str, self.Dict, self.List, self.Bool, self.Type, self.Tuple, self.Float])
        return function()

    def __int__(self, length: int = -1):
        return self.Int(length=length)

    def __str__(self, length: int = -1):
        return self.Str(length=length)

    def __float__(self, length: int = -1):
        return self.Float(length=length)

    def __bool__(self):
        return self.Bool()
