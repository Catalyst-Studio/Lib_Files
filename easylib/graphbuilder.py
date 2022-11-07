import matplotlib
from matplotlib import pyplot


def Set(x: list, y: list, label: str = None, linestyle: str = "-"):
    if len(x) != len(y):
        raise ValueError("Length of provided list does not match")
    return {
        "x": x,
        "y": y,
        "label": label,
        "linestyle": linestyle
    }


def Graph(*args):
    return [graph for graph in args]


class Graphbuilder:
    """Used to build and display graphs visually"""
    graphlist = []
    valid_shapes = ["rectangle", "square"]

    def __init__(self, shape: str = "rectangle", plotEngine: str = 'TkAgg'):
        """Sets the shape of the provided graphs and changes the engine that the graphing engine uses"""
        if shape not in self.valid_shapes:
            raise ValueError(
                """Shape provided is not a valid shape
                valid shapes:
                    square
                    rectangle"""
            )
        else:
            self.shape = shape
        matplotlib.use(plotEngine)

    def append(self, graph: list):
        """Add a graph to be displayed later"""
        self.graphlist.append(graph)

    def export(self):
        """Export the graph list"""
        return self.graphlist

    def pop(self, index: int = 0):
        """pop a graph from the graphs, works the same as a standard list pop function"""
        item = self.graphlist.pop(index)
        return item

    def remove(self, item: list):
        """remove an item from the graphs, works the same as a standard list remove function"""
        item = self.graphlist.remove(item)
        return item

    def build(self):
        total_length = len(self.graphlist)
        if total_length % 2 != 0:
            odd = True
            total_length = total_length - 1
        else:
            odd = False
        if self.shape == "rectangle":
            pair = [2, total_length / 2]
        elif self.shape == "square":
            divider = 2
            xy = {}
            while (total_length / divider).is_integer():
                xy[divider] = total_length / divider
                divider = divider * 2
            pairs = {}
            for x in xy:
                pairs[abs(int(x) - int(xy[x]))] = [x, int(xy[x])]
            y = 0
            for x in pairs:
                if x > y:
                    y = x
            for c in pairs:
                if c < y:
                    y = c
            pair = pairs[y]
        else:
            raise ValueError(
                """Shape provided is not a valid shape
                valid shapes:
                    square
                    rectangle"""
            )
        if odd:
            pair[0] = pair[0] + 1
        pairs = []
        figure, axis = pyplot.subplots(int(pair[1]), int(pair[0]))
        for i in range(0, int(pair[0])):
            for x in range(0, int(pair[1])):
                pairs.append([i, x])
        pairsRemoveAmount = len(pairs) - (total_length + 1)
        for t in range(0, pairsRemoveAmount):
            pairs.pop(-1)
        for x in pairs:
            index = pairs.index(x)
            graphs = self.graphlist[index]
            labelSet = False
            for graph in graphs:
                axis[x[1], x[0]].plot(graph["x"], graph["y"])
                if not labelSet:
                    axis[x[1], x[0]].set_title(graph["label"])
                    labelSet = True

        pyplot.show()
