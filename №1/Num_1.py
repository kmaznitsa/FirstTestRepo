if __name__ == '__main__':
    file = open('input.txt', mode='r')
    numbers = [int(i) for i in file.read().split()]
    file.close()
    result = sum(numbers)
    file = open('output.txt', mode='w')
    file.write(str(result))
    file.close()

