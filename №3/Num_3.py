if __name__ == '__main__':
    with open('input.txt', 'r') as inp, open('output.txt', 'w') as out:
        num = int(inp.read())
        if num // 10 > 0:
            result = str(num // 10 * (num // 10 + 1)) + '25'
            out.write(result)
        else:
            out.write('25')
    