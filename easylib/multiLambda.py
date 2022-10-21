class multilambda:
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
        try:
            return self.function_list
        except Exception as e:
            print(e.with_traceback())
            return False

    def add_key(self, function: list):
        try:
            if function[1][0] == "$self":
                function[1][0] = self
            self.function_list.append([function[0], function[1]])
            return True
        except Exception as e:
            print(e.with_traceback())
            return False

    def remove_key(self, function: list):
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
        while function in self.function_list:
            if function in self.function_list:
                self.function_list.remove(function)
        return True

    def clear_keys(self):
        self.function_list = []
        self.is_empty = True
        return True

    def vars(self, var):
        return self.variables[var]


def builder(*functions) -> multilambda:
    instance = multilambda([])
    for x in functions:
        instance.add_key(x)
    return instance


def Parameter(*args) -> list:
    return [param for param in args]


def Function(function, params: list = None) -> list:
    if params is None:
        params = []
    return [function, params]

