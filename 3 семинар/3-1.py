def my_bin(a):
    bin = ''
    if a == 0:
        bin = '0'
    else:
        while a > 0:
            bin = str(a % 2) + bin
            a //= 2
    return bin
a = int(input())
print(my_bin(a))
print(bin(a)[2:])