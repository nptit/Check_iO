def letter_queue(commands):
    if not commands:
        return ''

    queue = list()
    for command in commands:
        com_num = command.split()
        if com_num[0] == 'PUSH':
            queue.append(com_num[1])
        elif com_num[0] == 'POP':
            try:
                queue.pop(0)
            except IndexError:
                pass
    return ''.join(queue) if queue else ''

if __name__ == '__main__':
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D",
                         "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
