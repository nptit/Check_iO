def checkio(numbers):
    # str_numbers = [str(a) for a in numbers]
    # chain = dict()
    # for num in str_numbers:
    #     if num not in chain:
    #         chain[num] = list()
    #     for num2 in str_numbers:
    #         match = 0
    #         for c, d in zip(num, num2):
    #             if c == d:
    #                 match += 1
    #         if match == 2:  # sum() above instead, get rid of match
    #             chain[num].append(num2)

    chain = {'991': ['921', '999'], '321': ['323', '329', '121', '921'],
             '123': ['323', '121', '125'], '999': ['991'],
             '323': ['123', '321', '329'], '921': ['991', '321', '121'],
             '329': ['323', '321'], '125': ['123', '121'],
             '121': ['123', '321', '921', '125']}
    master = list()

    def walk(key, results):
        results.append(key)
        if chain[key]:  # not empty
            for value in chain[key]:
                if value not in results:
                    walk(value, results)
        else:
            if results[0] == '123' and results[-1] == '999':
                master.append(results)

    walk('123', list())
    print(master)
    return chain

print(checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]))
# == [123, 121, 921, 991, 999], "First"
# print()
# print(checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777])) # == [111, 121, 127, 727, 777], "Second"
# print()
# print(checkio([456, 455, 454, 356, 656, 654]))

# if __name__ == '__main__':
#     assert checkio([123, 991, 323, 321, 329, 121, 921, 125, 999]) == [123, 121, 921, 991, 999], "First"
#     assert checkio([111, 222, 333, 444, 555, 666, 121, 727, 127, 777]) == [111, 121, 127, 727, 777], "Second"
#     assert checkio([456, 455, 454, 356, 656, 654]) == [456, 454, 654], "Third, [456, 656, 654] is correct too"
