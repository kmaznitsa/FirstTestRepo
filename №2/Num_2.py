if __name__ == '__main__':
    inp = open('input.txt', 'r')
    number = int(inp.read())
    inp.close()
    result = 0
    i = 1
    if number > 0:
        while i <= number:
            result += i
            i += 1
    else:
        while i >= number:
            result += i
            i -= 1
    out = open('output.txt', 'w')
    out.write(str(result))
    out.close()