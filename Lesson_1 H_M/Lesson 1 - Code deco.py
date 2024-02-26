import pathlib
import os
import random
import time
import timeit
import functools
from collections import OrderedDict
import requests
import sys

from time import sleep


def profile(msg='Elapsed time', file=sys.stdout):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            start = time.time()
            result = f(*args, **kwargs)
            print(msg, f'({f.__name__}): {time.time() - start}s', file=file)
            return result

        return deco

    return internal


def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                deco._cache[cache_key]['count'] += 1
                deco._cache.move_to_end(cache_key, last=True)
                return deco._cache[cache_key]['value']

            result = f(*args, **kwargs)
            # видаляємо якшо досягли ліміта
            if len(deco._cache) >= max_limit:
                count_min = min(deco._cache, key=lambda x: deco._cache[x]['count']) # Поиск минимального количества
                del deco._cache[count_min]
            deco._cache[cache_key] = {'value': result, 'count': 0} # Создаем словарь внутри словаря со счетчиком
            return result

        deco._cache = OrderedDict() # "_cache - это переменная
        return deco

    return internal


@profile(msg='Elapsed time')
@cache(max_limit=2)
def fetch_url(url, first_n=2):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://ithillel.ua')
fetch_url('https://dou.ua')
fetch_url('https://dou.ua')
fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://google.com')
fetch_url('https://google.com')
# fetch_url('https://ithillel.ua')
fetch_url('https://dou.ua')
fetch_url('https://dou.ua')
print(fetch_url._cache)
print(len(fetch_url._cache))