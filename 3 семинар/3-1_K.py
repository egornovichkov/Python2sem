def inverse_bits(binary):
    binary_str = str(binary)
    binary_list = list(binary_str)
    for i in range(len(binary_list)):
        if (i + 1) % 2 == 0:
            if binary_list[i] == '0':
                binary_list[i] = '1'
            else:
                binary_list[i] = '0'
    inverted_binary = ''.join(binary_list)
    decimal = int(inverted_binary, 2)
    return decimal
binary = int(input())
print(inverse_bits(binary))