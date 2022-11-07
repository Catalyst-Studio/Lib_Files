class multiLambda:
    function_list = []
    example_list_items = [abs, (1, 2)]
    variables = {}
    is_empty = True

    def setvar(self, name: any, value: any):
        self.variables[name] = value

    def getvar(self, name: any):
        return self.variables[name]

    def printvar(self, name: any, printtype: any = print):
        printtype(self.variables[name])

    def execute(self):
        responces = []
        for i in self.function_list:
            responces.append(i[0](*i[1]))

    def getvars(self):
        return self.variables

    def __init__(self, functions: list):
        """Initilizes the MultiLambda Class"""
        if not isinstance(functions, list):
            raise ValueError("Parameter for creations of a function must be a list")
        for x in range(len(functions)):
            if type(functions[x][0]) not in [type(lambda: print()), type(print)]:
                raise ValueError(
                    f"All elements of parameter list must be a function or built in function. Found {type(x)}")
            else:
                if not isinstance(functions[x][1], tuple):
                    raise ValueError(str(type(functions[x][1])))
                newtuple = list(functions[x][1])
                for y in range(len(newtuple)):
                    if newtuple[y] == "$self":
                        newtuple[y] = self
                newtuple = tuple(newtuple)
                self.function_list.append([functions[x][0], newtuple])
                self.is_empty = False

    def get_keys(self):
        """Returns a list of all the functions stored in the current MultiLambda class"""
        return self.function_list

    def add_key(self, function: list):
        """Adds a function to the MultiLambda class to be executed later"""
        try:
            if function[1][0] == "$self":
                function[1][0] = self
            self.function_list.append([function[0], function[1]])
            return True
        except Exception as e:
            print(e.with_traceback())
            return False

    def remove_key(self, function: list):
        """Removes the function provided from the MultiLambda class"""
        try:
            if function in self.function_list:
                item = self.function_list.remove(function)
                if len(self.function_list) == 0:
                    self.is_empty = True
                return item
            return False
        except Exception as e:
            print(e.with_traceback())
            return False

    def remove_all_keys(self, function: list):
        """Removes all functions of the function provided"""
        while function in self.function_list:
            if function in self.function_list:
                self.function_list.remove(function)
        return True

    def clear_keys(self):
        """Removes all of the functions in the MultiLambda class"""
        self.function_list = []
        self.is_empty = True
        return True

    def vars(self, var):
        """Returns a variable stored in the MultiLambda class"""
        return self.variables[var]


def builder(*functions) -> multilambda:
    """Will make a MultiLambda instance with the functions provided"""
    instance = multilambda([])
    for x in functions:
        instance.add_key(x)
    return instance


def Parameter(*args) -> list:
    """Will generate the parameters used in a function"""
    return [param for param in args]


def Function(function, params: list = None) -> list:
    """Will generate a function with the function and parameters provided"""
    if params is None:
        params = []
    return [function, params]

