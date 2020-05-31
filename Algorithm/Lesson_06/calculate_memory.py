import sys


def my_show(object):
    """Функция принимает объект, в том числе список
    и возвращает объем памяти который он занимает.

    Arguments:
        object {int, float, str, list} -- объект для которого измерятся объем памяти

    Returns:
        int -- объем памяти занимаемый входным объектом
    """
    size_of_object = 0
    if hasattr(object, '__iter__'):
        if not isinstance(object, str):
            for item in object:
                size_of_object += my_show(item)
        else:
            return sys.getsizeof(object)
    else:
        return sys.getsizeof(object)
    return size_of_object


def input_list(my_list):
    output = 0
    for item in my_list:
        output += my_show(item)
    return output