import json

class export(list):

    def add(self, object: type):
        otype = type(object)
        try:
            info = object.__export__()
        except AttributeError:
            info = str(object)
        self.append({
            "name": object.__class__.__name__,
            "type": otype,
            "information": info
        })

    def export(self):
        for export in self:
            exportstr = json.dumps(export)
            print(exportstr)
