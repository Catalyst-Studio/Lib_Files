from typing import Iterable
import random


def combine_list(items: list = None):
    """Combine all items from a list to string"""
    if items is None:
        return None
    else:
        word = ""
        for i in items:
            word = f"{word}{i}"
        return word


def flattenList(alist: list = None):
    """Will remove all internal lists in a list and make it one coherent list"""
    if alist is None:
        raise ValueError("Did not pass through a valid list to flatten")
    else:
        newlist = []
        for item in alist:
            if isinstance(item, list):
                newlist = newlist + flattenList(item)
            else:
                newlist.append(item)
        return newlist


def add_list(items: list, check: bool = True):
    """Will add all items in a list"""
    num: any = 0
    for i in items:
        if type(i) != int and check:
            raise ValueError("one or more items in list are not int")
        else:
            num = num + i
    return num


def to_dict(items: list):
    Dict = {}
    if len(items) % 2 != 0:
        raise ValueError("Number of items in list are not even")
    itemnum = 0
    for x in range(int(len(items) / 2)):
        item = items[itemnum + 1]
        key = items[itemnum]
        itemnum = itemnum + 2
        Dict[key] = item
    return Dict


class Import:

    def __init__(self, items: list):
        if items is None:
            raise ValueError("Did not pass through a valid list to print")
        else:
            self.List = items

    def append_list(self, items: list = None):
        if items is None:
            raise ValueError("Did not pass through valid list to append")
        else:
            self.List = self.List + items

    def append(self, item):
        if item is None:
            raise ValueError("Did not pass through a valid item to append")

    def pop(self, __index: int = 0):
        item = self.List.pop(__index=__index)
        return item

    def remove(self, __value=None):
        item = self.List.remove(__value=__value)
        return item

    def reverse(self):
        self.List.reverse()

    def clear(self):
        self.List.clear()

    def copy(self):
        return Import(self.List.copy())

    def __getitem__(self, item):
        return self.List[item]

    def count(self, __value):
        return self.List.count(__value)

    def flatten(self):
        self.List = flattenList(alist=self.List)

    def extend(self, __iterable: Iterable[__getitem__]):
        self.List.extend(__iterable)

    def __str__(self):
        return str(self.List)

    def __iter__(self):
        for elem in self.List:
            yield elem

    def add(self, check: bool = True):
        return add_list(items=self.List, check=check)

    def combine(self):
        return combine_list(items=self.List)

    def index(self, __value, __start, __stop):
        self.List.index(__value, __start, __stop)

    def to_dict(self):
        return to_dict(items=self.List)

    def split_to_list(self):
        newlist = []
        for x in self.List:
            newlist.append([x])
        return newlist
