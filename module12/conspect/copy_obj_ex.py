from copy import copy, deepcopy


class Expences:
    def __init__(self):
        self.data = {}
        self.places = []

    def __repr__(self):
        return f'Expences({repr(self.data)}, {repr(self.places)})'

    def spent(self, place, value):
        self.data[str(place)] = value
        self.places.append(place)

    def __copy__(self):
        copy_obj = Expences()
        copy_obj.data = self.data
        copy_obj.places = self.places
        return copy_obj

    def __deepcopy__(self, memo=None):
        memo = memo or {}
        copy_obj = Expences()
        memo[id(self)] = copy_obj
        copy_obj.data = deepcopy(self.data, memo)
        copy_obj.places = deepcopy(self.places, memo)
        return copy_obj


if __name__ == '__main__':
    e = Expences()
    e.spent('hotel', 100)
    e.spent('taxi', 10)
    print(e.places)
    print(e)

    e_copy = copy(e)
    print(e_copy is e)
    e_copy.spent('bar', 30)
    print(e.places)
    print(e_copy.places)
    print(e)
    print(e_copy)

    e_deepcopy = deepcopy(e)
    print(e_deepcopy is e)
    e_deepcopy.spent('airport', 300)
    print(e.places)
    print(e_deepcopy.places)
    print(e)
    print(e_deepcopy)
