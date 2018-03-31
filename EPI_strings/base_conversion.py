# Review recursive solution from book and complexity analysis


def convert_base(string, base1, base2):
    base10_int = 0
    digit_list = list(string)
    for i in range(len(digit_list)):
        digit_value = (ord(digit_list[-(i+1)]) - 48) * base1**i
        base10_int += digit_value

    base2_list = []
    mod_power = 1
    next_digit = 0
    while base2**mod_power <= base10_int:
        mod_power += 1

    mod_power -= 1

    while mod_power >= 0:
        next_digit = base10_int // (base2**mod_power)
        base2_list.append(chr(ord('0') + next_digit))
        base10_int -= next_digit * (base2**mod_power)
        mod_power -= 1

    return ''.join(base2_list)

if __name__ == '__main__':
    #value is 75
    base2_string = '1001011'
    base4_string = '1023'
    base6_string = '203'

    assert(convert_base(base2_string, 2, 4) == base4_string)
    assert(convert_base(base2_string, 2, 6) == base6_string)
    assert(convert_base(base4_string, 4, 2) == base2_string)
    assert(convert_base(base4_string, 4, 6) == base6_string)
    assert(convert_base(base6_string, 6, 2) == base2_string)
    assert(convert_base(base6_string, 6, 4) == base4_string)