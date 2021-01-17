from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, stock):
        self.stock = stock
        self._position = 0

    def __next__(self):
        try:
            value = self.stock[self._position]
        except IndexError:
            raise StopIteration()
        else:
            self._position += 1
            return value
