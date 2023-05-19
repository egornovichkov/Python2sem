def binary_to_hex(binary):
    hex_digits = '0123456789ABCDEF'
    decimal = 0
    deg = 0
    binary = str(binary)
    for digit in reversed(binary):
        decimal += int(digit) * (2 ** deg)
        deg += 1

    hex = ''

    while decimal > 0:
        remainder = decimal % 16
        hex = hex_digits[remainder] + hex
        decimal //= 16

    return hex