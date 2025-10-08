from min_heap import Student, Heap
import unittest


class TestHeap(unittest.TestCase):

    def test_init(self):
        students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)]
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        self.assertEqual(heap.is_empty(), False)

    def test_contains(self):
        students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)]
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        self.assertEqual(heap.contains(Student("Loginov Georgiy Alekseevich", 4215, 18, 1, 4.1)), False)
        self.assertEqual(heap.contains(Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)), True)

    def test_create_heap_from_list(self):
        students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)]
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        self.assertEqual(heap.is_empty(), False)
        self.assertEqual(heap._check_range(1), False)
        self.assertEqual(heap.get_size(), 1)

    def test_check_range(self):
        students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)]
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        self.assertEqual(heap._check_range(1), False)
        self.assertEqual(heap._check_range(0), True)

    def test_resize(self):
        students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5),
                                   Student("Loginov Georgiy Alekseevich", 4215, 18, 1, 4.1)]
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        heap._resize(3)
        heap.insert(Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5))
        self.assertEqual(heap.get_size(), 3)

    def test_is_empty(self):
        students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)]
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        self.assertEqual(heap.is_empty(), False)

    def test_get_size(self):
        students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)]
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        self.assertEqual(heap.get_size(), 1)

    def test_trickle_up(self):
        students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5),
                                   Student("Loginov Georgiy Alekseevich", 4215, 18, 1, 4.1)]
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        heap._resize(3)
        heap.insert(Student("Novikova Ekaterina Pavlovna", 4216, 19, 1, 4.9))
        self.assertEqual(heap.contains(Student("Novikova Ekaterina Pavlovna", 4216, 19, 1, 4.9)), True)
        heap.remove()
        self.assertEqual(heap.contains(Student("Loginov Georgiy Alekseevich", 4215, 18, 1, 4.1)), False)

    def test_trickle_down(self):
        students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5),
                                   Student("Loginov Georgiy Alekseevich", 4215, 18, 1, 4.1)]
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        heap.change(1, Student("Novikova Ekaterina Pavlovna", 4216, 19, 1, 4.9))
        self.assertEqual(heap.contains(Student("Loginov Georgiy Alekseevich", 4215, 18, 1, 4.1)), True)
        heap.remove()
        self.assertEqual(heap.contains(Student("Loginov Georgiy Alekseevich", 4215, 18, 1, 4.1)), False)

    def test_change(self):
        students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)]
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        heap.change(0, Student("Novikova Ekaterina Pavlovna", 4216, 19, 1, 4.9))
        self.assertEqual(heap.contains(Student("Novikova Ekaterina Pavlovna", 4216, 19, 1, 4.9)), True)
        self.assertEqual(heap.get_size(), 1)

    def test_insert(self):
        students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)]
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        heap._resize(2)
        heap.insert(Student("Novikova Ekaterina Pavlovna", 4216, 19, 1, 4.9))
        self.assertEqual(heap.contains(Student("Novikova Ekaterina Pavlovna", 4216, 19, 1, 4.9)), True)
        self.assertEqual(heap.get_size(), 2)

    def test_remove(self):
        students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)]
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        heap.remove()
        self.assertEqual(heap.is_empty(), True)

    def test_save(self):
        students: list[Student] = [Student("Novikova Ekaterina Pavlovna", 4216, 19, 1, 4.9)]
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        heap.save()
        students: list[Student] = heap.load()
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        self.assertEqual(heap.contains(Student("Novikova Ekaterina Pavlovna", 4216, 19, 1, 4.9)), True)
        self.assertEqual(heap.get_size(), 1)

    def test_load(self):
        students: list[Student] = [Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)]
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        heap.save()
        students: list[Student] = heap.load()
        heap: Heap[Student] = Heap[Student].create_heap_from_list(students)
        self.assertEqual(heap.contains(Student("Ivanov Ivan Ivanovich", 4209, 20, 2, 4.5)), True)
        self.assertEqual(heap.get_size(), 1)


if __name__ == '__main__':
    unittest.main()
