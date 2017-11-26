'''
example 변수안의 식만을 계산
'''


def calculator(str):
    number = []
    operation = []

    for x in str.replace(' ', ''):
        if x.isdigit():
            number.append(x)
        else:
            operation.append(x)

    nmbr_len = len(number)
    x = int(number[nmbr_len - 2])
    y = int(number[nmbr_len - 1])

    return formula(operation[0])(x, y)


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
        '1+1',
        '3-1',
        '4- 1',
        '5 +1',
        '5 * 2',
        '8/ 2',
    ]
    for e in example:
        result = calculator(e)
        print('calculation result : {} = {}({})'.format(e, int(result), result))
