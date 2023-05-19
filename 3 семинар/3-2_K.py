def oct_to_hex(oct):
    hex_digits = '0123456789ABCDEF'
    decimal = 0
    deg = 0
    oct = str(oct)
    for digit in reversed(oct):
        decimal += int(digit) * (8 ** deg)
        deg += 1

    hex = ''

    while decimal > 0:
        remainder = decimal % 16
        hex = hex_digits[remainder] + hex
        decimal //= 16

    return hex