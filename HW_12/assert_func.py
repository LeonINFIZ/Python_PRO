def new_format(number_str):
    result = ''
    count = 0
    for digit in reversed(number_str):
        if count and count % 3 == 0:
            result = '.' + result
        result = digit + result
        count += 1
    return result


assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")

print("OK")
