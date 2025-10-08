import unittest
from doubly_linked_list import DoubleLinkedList, Student, Car


class TestDoubleLinkedList(unittest.TestCase):

    def test_init(self):
        double_linked_list = DoubleLinkedList[Student]()
        self.assertEqual(double_linked_list.get_size(), 0)
        self.assertIsNone(double_linked_list._head)
        self.assertIsNone(double_linked_list._tail)

    def test_str(self):
        double_linked_list = DoubleLinkedList[Student]()
        expected_str = "Current state: []"
        self.assertEqual(str(double_linked_list), expected_str)

    def test_getitem(self):
        double_linked_list = DoubleLinkedList[Student]()
        double_linked_list.push_head(Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5))
        self.assertEqual(double_linked_list[0], (Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)))

    def test_delitem(self):
        double_linked_list = DoubleLinkedList[Student]()
        self.assertFalse(double_linked_list.__delitem__(0))

    def test_contains(self):
        double_linked_list = DoubleLinkedList[Student]()
        self.assertFalse(double_linked_list.__contains__(Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)))

    def test_get_size(self):
        double_linked_list = DoubleLinkedList[Student]()
        self.assertEqual(double_linked_list.get_size(), 0)

    def test_check_range(self):
        double_linked_list = DoubleLinkedList[Student]()
        double_linked_list.push_head(Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5))
        self.assertFalse(double_linked_list._check_range(-1))

    def test_is_empty(self):
        double_linked_list = DoubleLinkedList[Student]()
        self.assertTrue(double_linked_list.is_empty())

    def test_push_tail(self):
        double_linked_list = DoubleLinkedList[Student]()
        double_linked_list.push_tail(Student("Belyakov Petr Petrovich", 4213, 21, 3, 4.2))
        double_linked_list.push_tail(Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5))
        self.assertEqual(double_linked_list.get_size(), 2)
        self.assertEqual(double_linked_list[1], (Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)))

    def test_push_head(self):
        double_linked_list = DoubleLinkedList[Student]()
        double_linked_list.push_head(Student("Belyakov Petr Petrovich", 4213, 21, 3, 4.2))
        double_linked_list.push_tail(Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5))
        self.assertEqual(double_linked_list.get_size(), 2)
        self.assertEqual(double_linked_list[0], (Student("Belyakov Petr Petrovich", 4213, 21, 3, 4.2)))

    def test_insert(self):
        double_linked_list = DoubleLinkedList[Student]()
        double_linked_list.push_tail(Student("Belyakov Petr Petrovich", 4213, 21, 3, 4.2))
        double_linked_list.insert(0, Student("Akhipova Anna Aleksandrovna", 4217, 20, 1, 4.8))
        self.assertEqual(double_linked_list.get_size(), 2)
        self.assertEqual(double_linked_list[0], Student("Akhipova Anna Aleksandrovna", 4217, 20, 1, 4.8))

    def test_for_each(self):
        double_linked_list = DoubleLinkedList[Student]()
        double_linked_list.push_tail(Student("Belyakov Petr Petrovich", 4213, 21, 3, 4.2))

        def apply_function(data: Student):
            nonlocal total_sum
            total_sum += data.age
        total_sum = 0
        double_linked_list.for_each(apply_function)
        self.assertEqual(total_sum, 21)

    def test_reverse_for_each(self):
        double_linked_list = DoubleLinkedList[Student]()
        double_linked_list.push_tail(Student("Belyakov Petr Petrovich", 4213, 21, 3, 4.2))

        def apply_function(data: Student):
            nonlocal total_sum
            total_sum += data.age
        total_sum = 0
        double_linked_list.for_each(apply_function)
        self.assertEqual(total_sum, 21)

    def test_reverse(self):
        double_linked_list = DoubleLinkedList[Student]()
        double_linked_list.reverse()
        self.assertEqual(double_linked_list.get_size(), 0)

    def test_sort_fio(self):
        double_linked_list = DoubleLinkedList[Student]()
        double_linked_list.push_head(Student("Belyakov Petr Petrovich", 4213, 21, 3, 4.2))
        double_linked_list.push_head(Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5))
        double_linked_list.sort_fio()
        self.assertEqual(double_linked_list[0], Student("Belyakov Petr Petrovich", 4213, 21, 3, 4.2))

    def test_sort_course(self):
        double_linked_list = DoubleLinkedList[Student]()
        double_linked_list.push_head(Student("Belyakov Petr Petrovich", 4213, 21, 3, 4.2))
        double_linked_list.push_head(Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5))
        double_linked_list.sort_course()
        self.assertEqual(double_linked_list[0], Student("Belyakov Petr Petrovich", 4213, 21, 3, 4.2))

    def test_sort_engine_capacity(self):
        double_linked_list = DoubleLinkedList[Car]()
        double_linked_list.push_head(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))
        double_linked_list.push_tail(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55))
        double_linked_list.sort_engine_capacity()
        self.assertEqual(double_linked_list[0], Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55))

    def test_sort_average_speed(self):
        double_linked_list = DoubleLinkedList[Car]()
        double_linked_list.push_head(Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))
        double_linked_list.push_head(Car("Ford", "1FA6P0H78G5112357", 2.0, 22000, 55))
        double_linked_list.sort_average_speed()
        self.assertEqual(double_linked_list[0], Car("Toyota", "JT2BF22K610038827", 2.4, 25000, 60))


if __name__ == '__main__':
    unittest.main()
