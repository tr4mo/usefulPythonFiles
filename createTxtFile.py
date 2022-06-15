string = input("Type your string: ")

path = 'file.txt'

try:
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(string)
except FileNotFoundError:
    print('Path ' + path + ' does not exist.')