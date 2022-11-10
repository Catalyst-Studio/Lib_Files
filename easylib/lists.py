from typing import Iterable
import random


def combine_list(items: list = None):
    """
    It takes a list of strings and returns a single string that is the concatenation of all the strings in the list

    :param items: list = None
    :type items: list
    :return: the word that is created by combining the items in the list.
    """
    if items is None:
        return None
    else:
        word = ""
        for i in items:
            word = f"{word}{i}"
        return word


def flattenList(alist: list = None):
    """
    It takes a list, and if it finds a list within that list, it will recursively call itself to flatten that list, and then
    add it to the original list

    :param alist: list = None
    :type alist: list
    :return: A list of all the items in the list, but with all the sublists flattened.
    """
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
    """
    `add_list` takes a list of integers and returns the sum of the list

    :param items: list - this is the list of items to be added
    :type items: list
    :param check: bool = True, defaults to True
    :type check: bool (optional)
    :return: The sum of all the items in the list.
    """
    num: any = 0
    for i in items:
        if type(i) != int and check:
            raise ValueError("one or more items in list are not int")
        else:
            num = num + i
    return num


def to_dict(items: list):
    """
    It takes a list of items and returns a dictionary with the first item in the list as the key and the second item as the
    value

    :param items: list
    :type items: list
    :return: A dictionary
    """
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


class Import(list):

    def __init__(self, items: list):
        """
        The function takes in a list and checks if it is empty. If it is empty, it raises a ValueError. If it is not empty,
        it assigns the list to the variable List

        :param items: list
        :type items: list
        """
        if items is None:
            raise ValueError("Did not pass through a valid list to print")
        else:
            self.List = items

    def append_list(self, items: list = None):
        """
        If the list is empty, raise an error. Otherwise, append the list

        :param items: list = None
        :type items: list
        """
        if items is None:
            raise ValueError("Did not pass through valid list to append")
        else:
            self.List = self.List + items

    def copy(self):
        """
        It returns a copy of the list.
        :return: A copy of the list.
        """
        return Import(self.List.copy())


    def flatten(self):
        """
        It takes a list of lists and returns a list of all the elements in the list of lists
        """
        self.List = flattenList(alist=self.List)


    def add(self, check: bool = True):
        """
        This function takes a list of items and adds them together

        :param check: If True, the function will check if the item already exists in the list. If it does, it will not add
        it, defaults to True
        :type check: bool (optional)
        :return: The return value is the number of items added to the list.
        """
        return add_list(items=self.List, check=check)

    def combine(self):
        """
        It takes a list of strings, and returns a string that is the concatenation of all the strings in the list
        :return: the result of the combine_list function.
        """
        return combine_list(items=self.List)

    def to_dict(self):
        """
        It takes a list of objects and returns a dictionary of dictionaries
        :return: A dictionary of the list of items.
        """
        return to_dict(items=self.List)

    def split_to_list(self):
        """
        It takes a list of lists and returns a list of lists where each element is a list of one element
        :return: A list of lists.
        """
        newlist = []
        for x in self.List:
            newlist.append([x])
        return newlist
