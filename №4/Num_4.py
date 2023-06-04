if __name__ == '__main__':
    with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
        num = int(inp.read())
        result = str(num) + '9' + '{}'.format(9 - num)
        out.write(result)