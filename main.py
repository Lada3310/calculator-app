def count_split(split):
    stroka = split.split()
    print(stroka)
    return len(stroka)

print(count_split(str(input('enter your stroka'))))
