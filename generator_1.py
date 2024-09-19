# Задание № 3

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.list_index = 0
        self.list_element_index = 0

    def __iter__(self):
        return self

    def __next__(self):

        while self.list_index < len(self.list_of_list):

            if self.list_element_index < len(self.list_of_list[self.list_index]):
                element = self.list_of_list[self.list_index][self.list_element_index]
                self.list_element_index += 1
                return element
            else:
                self.list_element_index = 0
                self.list_index += 1

        raise StopIteration

def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()