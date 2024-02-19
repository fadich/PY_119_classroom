from typing import (
    Optional,
    Any,
)


class Category:
    def __init__(self, name: str, parent: Optional["Category"] = None):
        self.name = name
        self._children = []
        self._parent = parent
        if self.parent is not None:
            self._parent._children.append(self)

    def __str__(self):
        return self.name

    @property
    def parent(self):
        return self._parent

    @property
    def children(self):
        return self._children


def print_tree(category: Category, ident: int = 0):
    print('--' * ident, category)
    for child in category.children:
        # print(f"  {child}")
        print_tree(child, ident + 1)


if __name__ == '__main__':
    strings = Category("strings", parent=None)
    beats = Category("beats", parent=None)
    guitars = Category("guitars", parent=strings)
    violins = Category("violins", parent=strings)
    drums = Category("drums", parent=beats)
    acoustics = Category("acoustics", parent=guitars)
    electrics = Category("electrics", parent=guitars)
    alt = Category("alt", parent=violins)
    fenders = Category("fenders", parent=electrics)
    gibsons = Category("gibsons", parent=electrics)

    print(electrics)
    print(electrics.parent)
    print(electrics.parent.parent)
    print(electrics.parent.parent.parent)

    print()
    print_tree(strings, 1)
    beats = Category("beats", parent=strings)
    drums = Category("drums", parent=beats)
    print_tree(strings, 1)
