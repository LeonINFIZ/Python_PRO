import codewars_test as test
import string

# https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    result_list = []

    alphabet = string.ascii_lowercase + string.ascii_uppercase

    word = ""
    count = 0

    for char in sentence:
        if char in alphabet:
            word += char
        else:
            result_list.append(word)
            word = ""
            result_list.append(char)

        if count == len(sentence) - 1:
            result_list.append(word)

        count += 1

    for i in range(len(result_list)):
        if len(result_list[i]) > 4:
            result_list[i] = result_list[i][::-1]

    return "".join(result_list)


print(spin_words("Welco"))  # This ecnetnes is a ecnetnes

#
# @test.describe("Stop gninnipS My sdroW!")
# def fixed_tests():
#     @test.it("Single word")
#     def _():
#         test.assert_equals(spin_words("Welcome"), "emocleW")
#         test.assert_equals(spin_words("to"), "to")
#         test.assert_equals(spin_words("CodeWars"), "sraWedoC")
#
#     @test.it("Multiple words")
#     def _():
#         test.assert_equals(spin_words("Hey fellow warriors"), "Hey wollef sroirraw")
#         test.assert_equals(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes")
