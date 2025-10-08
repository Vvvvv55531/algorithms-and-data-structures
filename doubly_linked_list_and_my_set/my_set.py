from typing import TypeVar, Generic, Dict, Callable

T = TypeVar("T", int, str)

MySetType = Dict[T, None]


class MySet(Generic[T]):

    def __init__(self, *arg) -> None:
        self._set: MySetType = {}
        if len(arg) == 0:
            return
        for it in list(arg):
            self.add(it)

    def __contains__(self, value: T) -> bool:
        return value in self._set

    def contains(self, value: T) -> bool:
        return value in self._set

    def add(self, value: T) -> bool:
        length = len(self._set)
        self._set[value] = None
        return length != len(self._set)

    def is_empty(self) -> bool:
        return len(self._set) == 0

    def size(self) -> int:
        return len(self._set)

    def remove_all(self) -> None:
        self._set: MySetType = {}

    def difference(self, other: 'MySet[T]') -> 'MySet[T]':
        new_set: MySet[T] = MySet()
        for k in self._set.keys():
            if not other.contains(k):
                new_set.add(k)

        return new_set

    def symmetric_difference(self, other: 'MySet[T]') -> 'MySet[T]':
        new_set: MySet[T] = MySet()
        for k in self._set.keys():
            if not other.contains(k):
                new_set.add(k)
        for k in other._set.keys():
            if not self.contains(k):
                new_set.add(k)
        return new_set

    def intersect(self, other: 'MySet[T]') -> 'MySet[T]':
        new_set: MySet[T] = MySet()
        if self.size() < other.size():
            for k in self._set.keys():
                if not other.contains(k):
                    new_set.add(k)
        else:
            for k in other._set.keys():
                if self.contains(k):
                    new_set.add(k)
        return new_set

    def union(self, other: 'MySet[T]') -> 'MySet[T]':
        new_set: MySet[T] = MySet()
        for k in self._set.keys():
            new_set.add(k)
        for k in other._set.keys():
            new_set.add(k)
        return new_set

    def is_subset(self, other: 'MySet[T]') -> bool:
        if other.size() < self.size():
            return False
        for k in self._set.keys():
            if not other.contains(k):
                return False
        return True

    def for_each(self, func: Callable[[T], None]) -> None:
        if self.size() == 0:
            return
        for k in self._set.keys():
            func(k)

    def print_set(self) -> None:
        print(list(self._set.keys()))
