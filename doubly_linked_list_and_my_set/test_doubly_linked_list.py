import unittest
from doubly_linked_list import DoubleLinkedList, Cat


class TestDoubleLinkedList(unittest.TestCase):

    def test_init(self):
        doubly_linked_list = DoubleLinkedList[Cat]()
        self.assertEqual(doubly_linked_list.get_size(), 0)
        self.assertIsNone(doubly_linked_list._head)
        self.assertIsNone(doubly_linked_list._tail)

    def test_str(self):
        doubly_linked_list = DoubleLinkedList[Cat]()
        expected_str = "Current state: []"
        self.assertEqual(str(doubly_linked_list), expected_str)

    def test_getitem(self):
        doubly_linked_list = DoubleLinkedList[Cat]()
        doubly_linked_list.push_head(Cat("Max", 4))
        self.assertEqual(doubly_linked_list[0], (Cat("Max", 4)))

    def test_delitem(self):
        doubly_linked_list = DoubleLinkedList[Cat]()
        self.assertFalse(doubly_linked_list.__delitem__(0))

    def test_contains(self):
        doubly_linked_list = DoubleLinkedList[Cat]()
        self.assertFalse(doubly_linked_list.__contains__(Cat("Max", 4)))

    def test_get_size(self):
        doubly_linked_list = DoubleLinkedList[Cat]()
        self.assertEqual(doubly_linked_list.get_size(), 0)

    def test_check_range(self):
        doubly_linked_list = DoubleLinkedList[Cat]()
        doubly_linked_list.push_head(Cat("Max", 4))
        self.assertFalse(doubly_linked_list._check_range(-1))

    def test_is_empty(self):
        doubly_linked_list = DoubleLinkedList[Cat]()
        self.assertTrue(doubly_linked_list.is_empty())

    def test_push_tail(self):
        doubly_linked_list = DoubleLinkedList[Cat]()
        doubly_linked_list.push_tail(Cat("Alex", 5))
        doubly_linked_list.push_tail(Cat("Max", 4))
        self.assertEqual(doubly_linked_list.get_size(), 2)
        self.assertEqual(doubly_linked_list[1], (Cat("Max", 4)))

    def test_push_head(self):
        doubly_linked_list = DoubleLinkedList[Cat]()
        doubly_linked_list.push_head(Cat("Alex", 5))
        doubly_linked_list.push_tail(Cat("Max", 4))
        self.assertEqual(doubly_linked_list.get_size(), 2)
        self.assertEqual(doubly_linked_list[0], (Cat("Alex", 5)))

    def test_insert(self):
        doubly_linked_list = DoubleLinkedList[Cat]()
        doubly_linked_list.push_tail(Cat("Alex", 5))
        doubly_linked_list.insert(0, Cat("Tommy", 1))
        self.assertEqual(doubly_linked_list.get_size(), 2)
        self.assertEqual(doubly_linked_list[0], Cat("Tommy", 1))

    def test_for_each(self):
        doubly_linked_list = DoubleLinkedList[Cat]()
        doubly_linked_list.push_tail(Cat("Alex", 5))

        def apply_function(data: Cat):
            nonlocal total_sum
            total_sum += data.age
        total_sum = 0
        doubly_linked_list.for_each(apply_function)
        self.assertEqual(total_sum, 5)

    def test_reverse_for_each(self):
        doubly_linked_list = DoubleLinkedList[Cat]()
        doubly_linked_list.push_tail(Cat("Alex", 5))

        def apply_function(data: Cat):
            nonlocal total_sum
            total_sum += data.age
        total_sum = 0
        doubly_linked_list.for_each(apply_function)
        self.assertEqual(total_sum, 5)

    def test_reverse(self):
        doubly_linked_list = DoubleLinkedList[Cat]()
        doubly_linked_list.reverse()
        self.assertEqual(doubly_linked_list.get_size(), 0)


if __name__ == '__main__':
    unittest.main()
