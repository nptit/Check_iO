cow = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


def cowsay(text):
    text = ' '.join(text.split())
    length = len(text)
    if length <= 39:
        return '\n {}\n< {} >\n {}{}'.format('_' * (length + 2), text,
                                             '-' * (length + 2), cow)
    else:
        lines = list()
        start = 0
        end = 39
        longest = 0
        # spaces = [index for index, char in enumerate(text) if char.isspace()]
        while True:
            if end >= length:
                lines.append(text[start:end])
                break
            elif text[end].isspace():
                lines.append(text[start:end])
                start = end + 1
                end += 40
            else:
                end = text.rfind(' ', start, end)
                lines.append(text[start:end])
                start = end + 1
                end += 40
            chunk = text[start:end]
            chunk_len = len(chunk)
            if chunk_len > longest:
                longest = chunk_len

        adjusted_lines = list()
        total_lines = len(lines)
        adjusted_lines.append(' {}'.format('_' * (longest + 2)))
        for index, line in enumerate(lines):
            line_len = len(line) - 1
            if index == 0:
                left, right = '/', '\\'
            elif index == total_lines - 1:  # last line
                left, right = '\\', '/'
            else:
                left, right = '|', '|'
            adjusted_lines.append('{} {} {: >{}}'.format(left, line, right,
                                                         longest - line_len))
        adjusted_lines.append(' {}'.format('-' * (longest + 2)))
        return '\n{}{}'.format('\n'.join(adjusted_lines), cow)

if __name__ == '__main__':
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines

    cowsay_many_lines = cowsay(
        'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
        'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines
