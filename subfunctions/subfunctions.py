from difflib import Differ


def compare_and_print(first, second):
    d = Differ()
    delta = list(d.compare(first.split('\n'), second.split('\n')))
    print('\n')
    print(''.join(delta))
