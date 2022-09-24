import builtins
import datetime


def split(word: str = None):
    """Splits a word into a list for each character"""
    return [char for char in word]


# dict class


def timestamp_print(*args, sep: str = None, end: str = None, file=None, flush: bool = False,
                    time_format: str = "%Y-%m-%d %H:%M:%S"):
    """Makes all print statements print with the time in front of them"""
    print()
    print_statement = ""
    timeprint = datetime.datetime.now().strftime(time_format)
    for i in args:
        print_statement = f"{print_statement}{i}"
    builtins.print(f"{timeprint}: {print_statement}", sep=sep, end=end, file=file, flush=flush)


class graphbuilder:
    """Used to build and display graphs visually"""
    graphlist = []

    def append(self, x: list = None, y: list = None):
        """Add a graph to be displayed later"""
        if x is None:
            raise ValueError("Did Not pass through valid list for x coordinates")
        elif y is None:
            raise ValueError("Did not pass through valid list for x coordinates")
        elif len(x) != len(y):
            raise ValueError("Length of list do not match")
        item_list = [x, y]
        self.graphlist.append(item_list)

    def export(self):
        """Export the graph list"""
        return self.graphlist

    def pop(self, index: int = 0):
        """pop a graph from the graphs, works the same as a standard list pop function"""
        item = self.graphlist.pop(index)
        return item

    def remove(self, item: list = None):
        """remove an item from the graphs, works the same as a standard list remove function"""
        if item is None:
            raise ValueError("Did not pass through a valid list to remove")
        else:
            item = self.graphlist.remove(item)
            return item
