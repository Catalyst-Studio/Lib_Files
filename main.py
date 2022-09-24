from easylib import lib
from sys import setrecursionlimit
from easylib import lib, lists, dictionaries, multiLambda
from easylib.lib import timestamp_print as print

setrecursionlimit(5000)
items = lists.rand_gen(20, type=int)
params = multiLambda.parameter_constructor("hello", "world")
function = multiLambda.function_constructor(function=print, params=params)
functions = multiLambda.functions_builder(function)
functions = multiLambda.builder(functions=functions)
functions.setvar(name="hello", value="world")
test = functions.getvar("hello")
print(test)
