import functools

from pympler import asizeof


def memory(msg='memory size'):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            result = f(*args, **kwargs)
            size = asizeof.asizeof(result)
            print(msg, f'({f.__name__}): memory size: {size})')
            return result

        return deco

    return internal


@memory(msg='Memory')
def create_100_element_list(a):
    empty_lst = []
    for i in range(a):
        empty_lst.append(i)
    return empty_lst


create_100_element_list(200)
