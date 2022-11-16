from easylib.exporter import export
from easylib.age import Age, Birthdate

page = Age(Birthdate(2006, 12, 23))

exporter = export()

exporter.add(page)
print(exporter)
