def digit_stack(lst):
    if not lst:
        return 0

    stack = list()
    total = 0
    for command in lst:
        com_num = command.split()
        if com_num[0] == 'PUSH':
            stack.append(int(com_num[1]))
        elif com_num[0] == 'POP':
            try:
                total += int(stack.pop())
            except IndexError:
                pass
        elif com_num[0] == 'PEEK':
            try:
                total += int(stack[-1])
            except IndexError:
                pass
    return total

if __name__ == '__main__':
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
