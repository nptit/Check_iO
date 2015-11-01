def checkio(pattern, image):
    pat_width = len(pattern[0])  # in case width and height are different
    pat_height = len(pattern)
    image_width = len(image[0])
    image_height = len(image)

    for a in range(image_height):
        for b in range(image_width):
            check_pattern = list()      # list of lists of chunk of image
            check_coordinates = list()  # list for x and y coordinates
            for c in range(pat_height):
                check_row = list()      # each row of check pattern
                curr_x = a + c
                for d in range(pat_width):
                    curr_y = d + b
                    if 0 <= curr_x < image_height and \
                       0 <= curr_y < image_width:
                        check_coordinates.append((curr_x, curr_y))
                        check_row.append(image[curr_x][curr_y])
                check_pattern.append(check_row)

            if check_pattern == pattern:
                for e, f in check_coordinates:  # alter values in image
                    if image[e][f] == 0:
                        image[e][f] = 2
                    else:
                        image[e][f] = 3
    return image

if __name__ == '__main__':
    assert checkio([[1, 0], [1, 1]],
                   [[0, 1, 0, 1, 0],
                    [0, 1, 1, 0, 0],
                    [1, 0, 1, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 1, 1, 0, 0]]) == [[0, 3, 2, 1, 0],
                                          [0, 3, 3, 0, 0],
                                          [3, 2, 1, 3, 2],
                                          [3, 3, 0, 3, 3],
                                          [0, 1, 1, 0, 0]]
    assert checkio([[1, 1], [1, 1]],
                   [[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]]) == [[3, 3, 1],
                                    [3, 3, 1],
                                    [1, 1, 1]]
    assert checkio([[0, 1, 0], [1, 1, 1]],
                   [[0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                    [0, 1, 1, 1, 0, 0, 0, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 1, 0, 1, 0],
                    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
                    [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                    [0, 1, 1, 0, 0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) == \
        [[0, 2, 3, 2, 0, 0, 0, 2, 3, 2],
         [0, 3, 3, 3, 0, 0, 0, 3, 3, 3],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 2, 3, 2, 0, 0, 0],
         [2, 3, 2, 0, 3, 3, 3, 0, 1, 0],
         [3, 3, 3, 0, 0, 0, 0, 0, 1, 1],
         [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 2, 3, 2, 0],
         [0, 1, 1, 0, 0, 0, 3, 3, 3, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
