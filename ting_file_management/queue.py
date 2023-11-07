from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        if self.__len__ == 0:
            return None
        else:
            return self._data.pop(0)

    def search(self, index):
        if index < 0 or index > len(self._data) - 1:
            raise IndexError("Índice Inválido ou Inexistente")
        return self._data[index]
