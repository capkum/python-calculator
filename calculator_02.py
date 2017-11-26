'''
example 변수안의 식만을 계산
문제점 * + 등이 혼용되면 문제 발생
'''


def calculator(str):
    numbers = []
    operations = []

    for x in str.replace(' ', ''):
        if x.isdigit():
            numbers.append(x)
        else:
            operations.append(x)

    while operations:
        operation = operations.pop(0)
        x = int(numbers.pop(0))
        y = int(numbers.pop(0))

        numbers.insert(0, formula(operation)(x, y))

    return numbers[0]


def formula(opr):
    calcu = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
    }

    return calcu[opr]


if __name__ == '__main__':
    example = [
        '1+1 + 1',
        '3-1 + 7',
        '3+1 - 7',
        '4- 1',
        '5 +1',
        '5 * 2',
        '8/ 2',

    ]
    for e in example:
        result = calculator(e)
        print('calculation result : {} = {}({})'.format(e, int(result), result))
