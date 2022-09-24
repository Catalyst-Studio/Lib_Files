def dict_to_list(items: dict = None, split: bool = True):
    """Will split a dictionary two to list of the keys and the values of the corresponding keys"""
    if items is None:
        return None
    else:
        if split:
            keys_list = []
            items_list = []
            for i in items:
                keys_list.append(i)
                items_list.append(items[i])
            return [keys_list, items_list]
        elif not split:
            items_r = []
            for i in items:
                items_r.append(i)
                items_r.append(items[i])
            return items_r

class dictionary_worker:
    """Class to do multiple things to the same dictionary more efficiently"""
    __doc__ = "Class to do multiple things to the same dictionary more efficiently"

    def __init__(self, dictionary: dict = None):
        if dictionary is None:
            raise ValueError("Dictionary not specified")
        else:
            self.dictionary = dictionary

    def __getitem__(self, item):
        return self.dictionary[item]

    def to_list(self, split: bool = True):
        """Will return the converted dictionary to list"""
        return dict_to_list(items=self.dictionary, split=split)