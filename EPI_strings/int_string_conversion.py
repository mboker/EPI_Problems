

def string_to_int(string):
    digit_list = list(string)
    is_negative = False
    index = 0
    if digit_list[0] == '-':
        is_negative = True
        index = 1

    int_value = 0
    while index < len(digit_list):
        int_value *= 10
        int_value += ord(digit_list[index]) - 48
        index += 1

    if is_negative:
        int_value *= -1

    return int_value


def int_to_string(int):
    chars = []
    is_negative = False
    if int < 0:
        is_negative = True
        int *= -1

    if int == 0:
        return chr(ord('0'))

    while int > 0:
        lowest_digit = int % 10
        chars.append(chr(ord('0') + lowest_digit))
        int //= 10

    if is_negative:
        chars.append('-')

    chars.reverse()
    return ''.join(chars)


if __name__ == '__main__':
    string_rep = '4231'
    int_rep = 4231

    assert(string_rep == int_to_string(int_rep))
    assert(int_rep == string_to_int(string_rep))

    negative_string_rep = '-4231'
    negative_int_rep = -4231

    assert(negative_string_rep == int_to_string(negative_int_rep))
    assert(negative_int_rep == string_to_int(negative_string_rep))

    zero_string_rep = '0'
    zero_int_rep = 0

    assert(negative_string_rep == int_to_string(negative_int_rep))
    assert(negative_int_rep == string_to_int(negative_string_rep))

