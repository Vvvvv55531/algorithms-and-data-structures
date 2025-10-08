from single_linked_list import SingleLinkedList
import ctypes
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import TypeVar, Generic, Optional, Callable


class IKey(ABC):

    @abstractmethod
    def key(self) -> int:
        ...


T = TypeVar("T", bound=IKey)


class HeapOverFlowException(Exception):
    pass


class EmptyHeapException(Exception):
    pass


class IndexOutRangeException(Exception):
    pass


@dataclass
class Car(IKey):
    stamp: str
    vin: str
    engine_capacity: float
    cost: int
    average_speed: int

    def key(self) -> int:
        return self.cost

    def __str__(self) -> str:
        return f"{self.stamp}, {self.vin}, {self.engine_capacity}, {self.cost}, {self.average_speed}"


class Heap(Generic[T]):

    def __init__(self, size: int,
                 fixed: bool = False,
                 comp: Callable[[T, T], bool] = lambda a, b: a.key() < b.key()) -> None:
        self._length: int = 0
        self._capacity: int = size
        self._is_fixed: bool = fixed
        self._comp: Callable[[T, T], bool] = comp
        self._arr: ctypes.Array[Optional[T]] = (size * ctypes.py_object)()
        for var in range(0, size):
            self._arr[var] = None

    def __contains__(self, item: T) -> bool:
        data = self._arr
        for element in range(0, self._length):
            if data[element] == item:
                return True
        return False

    def contains(self, item: T) -> bool:
        data: ctypes.Array[Optional[T]] = self._arr
        for element in range(0, self._length):
            if data[element] == item:
                return True
        return False

    @staticmethod
    def create_heap_from_list(data: SingleLinkedList[Car],
                              fixed: bool = True,
                              comp: Callable[[T, T], bool] = lambda b, a: a.key() < b.key()) -> 'Heap[T]':
        struct: Heap[T] = Heap[T](size=data.get_size(), fixed=fixed, comp=comp)

        data.for_each(struct.insert)

        return struct

    def _check_range(self, index: int) -> bool:
        if index >= self._length or index < 0:
            return False
        return True

    def _resize(self, new_capacity: int) -> None:
        new_array: ctypes.Array[T] = (new_capacity * ctypes.py_object)()
        for it in range(self._length):
            new_array[it] = self._arr[it]

        self._arr = new_array
        self._capacity = new_capacity

    def is_empty(self) -> bool:
        return self._length == 0

    def get_size(self) -> int:
        return self._length

    def trickle_up(self, index: int) -> None:
        parent: int = (index - 1) // 2
        bottom: T = self._arr[index]

        while index > 0 and self._comp(self._arr[parent], bottom):
            self._arr[index] = self._arr[parent]
            index = parent
            parent = (parent - 1) // 2

        self._arr[index] = bottom

    def trickle_down(self, index: int) -> None:
        large_child: int = 0
        top: T = self._arr[index]
        while index < self._length // 2:
            left_child: int = 2 * index + 1
            right_child: int = left_child + 1
            if (right_child > self._length and
                    self._comp(self._arr[large_child], self._arr[right_child])):
                large_child = right_child
            else:
                large_child = left_child

            if not self._comp(top, self._arr[large_child]):
                break

            # Потомок сдвигается вверх
            self._arr[index] = self._arr[large_child]
            index = large_child

        self._arr[index] = top  # index <- корень

    def change(self, index: int, new_value: T) -> None:
        ok: bool = self._check_range(index)
        if not ok:
            raise IndexOutRangeException("IndexOutRangeException")

        old_value: T = self._arr[index]
        self._arr[index] = new_value
        if self._comp(old_value, new_value):
            self.trickle_up(index)
        else:
            self.trickle_down(index)

    def insert(self, value: T) -> None:
        if self._length >= self._capacity:
            if self._is_fixed:
                raise HeapOverFlowException(f"StackOverFlowException: {value}")
            else:
                self._resize(self._capacity*2)

        self._arr[self._length] = value
        self.trickle_up(self._length)
        self._length += 1

    def remove(self) -> T:
        if self.is_empty():
            raise EmptyHeapException("EmptyHeapException")

        root: T = self._arr[0]
        self._length -= 1
        self._arr[0] = self._arr[self._length]
        self.trickle_down(0)
        return root

    def print_heap(self) -> None:
        print("heapArray: ")
        for it in range(0, self._length):
            if self._arr[it] is not None:
                print(f"{self._arr[it].key()} ", end='')
            else:
                print("-- ", end='')

        print("")

        n_blanks, items_per_row, column, j = (32, 1, 0, 0)
        dots: str = 32 * "."
        print(dots * 2)
        while self._length > 0:
            if column == 0:
                for it in range(0, n_blanks):
                    print(" ", end='')

            print(f"{self._arr[j].key()} ", end='')
            j += 1
            if j >= self._length:
                break

            column += 1
            if column == items_per_row:
                # Конец строки
                n_blanks //= 2  # Половина пробелов
                items_per_row *= 2  # Вдвое больше элементов
                column = 0  # Начать заново
                print("")  # Переход на новую строку
            else:
                for it in range(0, n_blanks * 2 - 2):
                    print(" ", end='')
        print("\n" + dots * 2)

    def save(self) -> None:
        with open("heap_save.txt", "w") as file:
            data: ctypes.Array[T] = self._arr
            for element in range(0, self._length):
                file.write(f"{data[element]}\n")

    @staticmethod
    def load() -> list[Car]:
        storage: list[Car] = []
        with (open("heap_save.txt", "r") as file):
            for line in file:
                string: str = line.strip()
                elements: list[str] = string.split(", ")  # Разделяем строку на части
                if len(elements) == 5:
                    stamp, vin, engine_capacity, cost, average_speed = elements
                    car = Car(str(stamp), str(vin), float(engine_capacity), int(cost), int(average_speed))
                    storage.append(car)
        return storage
