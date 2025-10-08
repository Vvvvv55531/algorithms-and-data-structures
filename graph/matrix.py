from typing import Union
import pickle


class Matrix:
    def __init__(self) -> None:
        self._matrix: list[list[Union[str, int]]] = []
        self._len: int = 0
        self._max_value: str = ""
        self._max_title: str = ""

    def __getitem__(self, index: int) -> list[str]:
        return self._matrix[index - 1]

    def get_matrix(self) -> list[list[Union[str, int]]]:
        return self._matrix

    def add_value(self, title1: str, title2: str, value: int) -> None:
        if self.title_check(title1) and self.title_check(title2):
            self._set_value(title1, title2, value)
            self._set_value(title2, title1, value)

            str_value = str(value)
            if len(str_value) > len(self._max_value):
                self._max_value = str_value
        else:
            raise ValueError("Title doesn't exist")

    def _set_value(self, v1: str, v2: str, w: int) -> None:
        index: int = 0

        for i in range(self._len):
            if self._matrix[i][0] == v1:
                index = i

        for i in range(self._len):
            if self._matrix[i][0] == v2:
                self._matrix[i][index + 1] = w

    def add_title(self, title: str) -> None:
        if self.title_check(title):
            raise ValueError("Title already exists")

        if len(title) > len(self._max_title):
            self._max_title = title

        if len(self._max_title) > len(self._max_value):
            self._max_value = self._max_title

        self._matrix.append([title])
        self._len += 1

        for current_title in range(self._len):
            while len(self._matrix[current_title]) != self._len + 1:
                self._matrix[current_title].append(0)

    def title_check(self, title: str) -> bool:
        for exist_title in range(self._len):
            if title == self._matrix[exist_title][0]:
                return True
        return False

    def length_check(self) -> bool:
        if self._len == 0:
            return True
        return False

    def print(self) -> None:
        if self.length_check():
            raise AttributeError("Matrix is empty")

        matrix_name: list[str] = []
        current_matrix: list[list[str]] = []

        for title in range(self._len):
            title_state: list[str] = [str(item) for item in self._matrix[title]]
            current_matrix.append(title_state)
            matrix_name.append(current_matrix[title][0])

        for name in range(self._len):
            if len(matrix_name[name]) < len(self._max_value):
                matrix_name[name] = (matrix_name[name]
                                     + " " * (len(self._max_value) -
                                              len(matrix_name[name])))

        for i in range(self._len):
            if len(current_matrix[i][0]) < len(self._max_title):
                current_matrix[i][0] = (current_matrix[i][0]
                                        + " " * (len(self._max_title) -
                                                 len(current_matrix[i][0])))

            for j in range(1, len(current_matrix[i])):
                if len(current_matrix[i][j]) < len(self._max_value):
                    current_matrix[i][j] = (current_matrix[i][j]
                                            + " " * (len(self._max_value) -
                                                     len(current_matrix[i][j])))

        matrix_name.insert(0, " " * len(self._max_title))
        print(matrix_name)

        for line in range(0, self._len - 1):
            print(current_matrix[line])
        print(current_matrix[self._len - 1])

    def clean(self) -> None:
        if self.length_check():
            raise AttributeError("Matrix is empty")

        self._matrix = []
        self._len = 0
        self._max_value = ""
        self._max_title = ""

    def save(self):
        matrix_save: list[list[str]] = self.get_matrix()

        with open("matrix_save.pkl", "wb") as file:
            pickle.dump(matrix_save, file)

    def load(self):
        with open("matrix_save.pkl", "rb") as file:
            matrix_load: list[list[str]] = pickle.load(file)

        for i in range(len(matrix_load)):
            self._len += 1

            if len(matrix_load[i][0]) > len(self._max_title):
                self._max_title = matrix_load[i][0]

            for j in range(len(matrix_load[i])):
                if len(str(matrix_load[i][j])) > len(self._max_value):
                    self._max_value = str(matrix_load[i][j])

        self._matrix = matrix_load
