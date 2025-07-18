def custom_map(data: dict, key_func, value_func):
    for key, value in data.items():
        yield (key_func(key), value_func(value))

d = {'a': 1, 'b': 2, 'c': 3}

result = custom_map(d, str.upper, lambda x: x * 10)

for k, v in result:
    print(k, v)
