'''
example 변수안의 식만을 계산
후위표기법 계산기
'''


def calculator(str):
    get_postfix = generator_postfix(str)
    numbers = []

    for dt in get_postfix:
        if dt.isdigit():
            numbers.append(dt)
        else:
            y = int(numbers.pop())
            x = int(numbers.pop())
            numbers.append(formula(dt)(x, y))

    return numbers[0]


# postfix후위 표기법으로 변환
def generator_postfix(str):

    postfix_stack = []
    oper_stack = []

    for dt in str.replace(' ', ''):
        if dt.isdigit():
            postfix_stack.append(dt)

        else:
            if len(oper_stack) == 0:
                oper_stack.append(dt)

            elif oper_priority(oper_stack[-1]) < oper_priority(dt):
                oper_stack.append(dt)

            elif oper_priority(oper_stack[-1]) == oper_priority(dt):
                postfix_stack.append(oper_stack.pop())
                oper_stack.append(dt)

            elif oper_priority(oper_stack[-1]) > oper_priority(dt):
                while oper_stack:
                    postfix_stack.append(oper_stack.pop())
                oper_stack.append(dt)

    if '*' in oper_stack or '%' in oper_stack:
        while oper_stack:
            postfix_stack.append(oper_stack.pop())
        oper_stack = []
    else:
        while oper_stack:
            postfix_stack.append(oper_stack.pop(0))
        oper_stack = []

    return postfix_stack


def oper_priority(opr):
    obj = {
        '*': 4,
        '/': 4,
        '+': 3,
        '-': 3,
    }
    return obj[opr]


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
        '9-5-5*2-2*9',
        '1*2+3',
        '1+2*3',
        '1+1 + 1',
        '3-1 + 7',
        '3+1 - 7',
        '4- 1',
        '5 +1',
        '5 * 2-1',
        '8/ 2 +2',
    ]
    for e in example:
        result = calculator(e)
        print('calculation result : {} = {}({})'.format(e, int(result), result))
