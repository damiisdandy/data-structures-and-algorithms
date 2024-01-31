import unittest
from .array import Array, ArrayOutOfIndex


class TestArray(unittest.TestCase):
    def test_init(self):
        _array = Array(1, 2, 3)
        self.assertEqual(_array.length, 3)
        self.assertDictEqual(_array.data, {0: 1, 1: 2, 2: 3})

    def test_push(self):
        _array = Array()
        self.assertEqual(_array.length, 0)
        _array.push("a")
        self.assertEqual(_array.length, 1)
        self.assertDictEqual(_array.data, {0: "a"})

    def test_get(self):
        _array = Array(1, 2)
        self.assertEqual(_array.get(0), 1)
        self.assertRaises(ArrayOutOfIndex, _array.get, -100)
        self.assertRaises(ArrayOutOfIndex, _array.get, 100)

    def test_pop(self):
        _array = Array("one", "two", "three")
        popped_value = "three"
        self.assertEqual(_array.pop(), popped_value)
        self.assertEqual(_array.length, 2)

    def test_delete(self):
        _array = Array("a", "b", "c", "d", "e")
        item_to_delete = _array.delete(2)
        self.assertEqual(item_to_delete, "c")
        self.assertDictEqual(_array.data, {0: "a", 1: "b", 2: "d", 3: "e"})
        self.assertEqual(_array.length, 4)

    def test_insert(self):
        _array = Array("a", "b", "d", "e")
        _array.insert(2, "c")
        self.assertDictEqual(_array.data, {0: "a", 1: "b", 2: "c", 3: "d", 4: "e"})
        self.assertEqual(_array.length, 5)


if __name__ == "__main__":
    unittest.main()
