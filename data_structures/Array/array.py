from typing import Any


class ArrayOutOfIndex(Exception):
    """Raise when array is out of index"""

    def __init__(self) -> None:
        super().__init__("Array is out of index")

    pass


class ArrayIsEmpty(Exception):
    """Raise when array is empty"""

    def __init__(self) -> None:
        super().__init__("Array is empty")

    pass


class Array:
    """A Data Structure that organizes items sequentially"""

    def __init__(self, *args) -> None:
        self.data = {}
        self.length = 0
        # initializing the array has a BigO of O(n)
        for index, value in enumerate(args):
            self.data[index] = value
            self.length += 1

    def get(self, index: int) -> Any:
        """Get item at specified index
        BigO: O(1)
        """
        if index < 0 or index >= self.length:
            raise ArrayOutOfIndex
        return self.data[index]

    def push(self, item: Any) -> None:
        """Add element to the end of the array
        BigO: O(1)
        """
        new_index = self.length
        self.data[new_index] = item
        self.length += 1
        return item

    def pop(self) -> Any:
        """Remove last element of array and return it
        BigO: O(1)
        """
        if self.length == 0:
            raise ArrayIsEmpty
        last_item = self.data[self.length - 1]

        del self.data[self.length - 1]
        self.length -= 1

        return last_item

    def _unshift(self, index: int) -> None:
        """Shift elements from index to the left
        BigO: O(n)
        """
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]

    def delete(self, index: int) -> Any:
        """Delete element by index from array
        BigO: O(n)
        """
        item_to_delete = self.get(index)
        self._unshift(index)

        # remove last element, the last and the one before it will be
        # duplicates due to the unshift
        del self.data[self.length - 1]
        self.length -= 1
        return item_to_delete

    def _shift(self, index: int) -> None:
        """Shift elements from index to the right
        BigO: O(n)
        """
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i - 1]

    def insert(self, index: int, value: Any) -> None:
        """Insert element at index of array
        BigO: O(n)
        """
        # insert within the scope of the array
        if index < 0 or index >= self.length:
            raise ArrayOutOfIndex
        self._shift(index)
        self.data[index] = value
        self.length += 1
