import unittest
from my_set import MySet


class TestMySet(unittest.TestCase):

    def test_init(self):
        my_set = MySet(1, 2)
        self.assertTrue(1 in my_set)
        self.assertTrue(2 in my_set)

    def test_contains(self):
        my_set = MySet()
        self.assertFalse(1 in my_set)

    def test_add(self):
        my_set = MySet()
        added = my_set.add(1)
        self.assertTrue(added)
        self.assertTrue(1 in my_set)

    def test_is_empty(self):
        my_set = MySet()
        self.assertTrue(my_set.is_empty())

    def test_size(self):
        my_set = MySet(1, 2)
        self.assertEqual(my_set.size(), 2)

    def test_remove_all(self):
        my_set = MySet(1, 2, 3)
        my_set.remove_all()
        self.assertEqual(my_set.size(), 0)

    def test_difference(self):
        my_set1 = MySet(1, 2)
        my_set2 = MySet(2, 4)
        result = my_set1.difference(my_set2)
        self.assertEqual(result.size(), 1)
        self.assertTrue(1 in result)
        self.assertFalse(2 in result)

    def test_symmetric_difference(self):
        my_set1 = MySet(1, 2)
        my_set2 = MySet(2, 4)
        result = my_set1.symmetric_difference(my_set2)
        self.assertEqual(result.size(), 2)
        self.assertTrue(1 in result)
        self.assertTrue(4 in result)
        self.assertFalse(2 in result)

    def test_intersect(self):
        my_set1 = MySet(1, 2)
        my_set2 = MySet(2, 4)
        result = my_set1.intersect(my_set2)
        self.assertEqual(result.size(), 1)
        self.assertFalse(1 in result)
        self.assertFalse(4 in result)
        self.assertTrue(2 in result)

    def test_union(self):
        my_set1 = MySet(1, 2)
        my_set2 = MySet(2, 4)
        result = my_set1.union(my_set2)
        self.assertEqual(result.size(), 3)
        self.assertTrue(1 in result)
        self.assertTrue(4 in result)
        self.assertTrue(2 in result)

    def test_is_subset(self):
        my_set1 = MySet(1, 2)
        my_set2 = MySet(1, 2, 4)
        self.assertTrue(my_set1.is_subset(my_set2))

    def test_for_each(self):
        my_set = MySet(1, 2, 4)
        results = MySet()

        def test_func(i):
            results.add(i)
        my_set.for_each(test_func)
        self.assertEqual(results.size(), 3)


if __name__ == '__main__':
    unittest.main()
