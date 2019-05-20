def to_string(n, base):
    convert_String = "0123456789ABCDEF"
    if n < base:
        return convert_String[n]
    else:
        return to_string(n//base, base)+convert_String[n % base]


# program

print(to_string(2835, 16))
