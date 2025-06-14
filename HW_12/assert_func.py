def new_format(number_str):
    result = ""
    count = 0
    for num in number_str[::-1]:
        if count %3 == 0 and count != 0:
            result += "."

        count += 1
        result += num

    return result[::-1]

assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")

print("OK")
