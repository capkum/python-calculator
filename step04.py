'''
example 변수안의 식만을 계산
목표: ()안의 수식 계산
'''


def calculator(str):
    get_postfix = generator_postfix(str)
    numbers = []

    for item in get_postfix:
        if item.isdigit():
            numbers.append(item)
        else:
            y = int(numbers.pop())
            x = int(numbers.pop())
            numbers.append(formula(item)(x, y))

    return numbers[0]


# postfix후위 표기법으로 변환
def generator_postfix(str):

    postfix_stack = []
    oper_stack = []

    for idx, item in enumerate(str.replace(' ', '')):
        if item.isdigit():
            postfix_stack.append(item)

        else:
            if len(oper_stack) == 0:
                oper_stack.append(item)
            
            elif oper_priority(item) > oper_priority(oper_stack[-1]):
                if ')' is not item:
                    oper_stack.append(item)

            elif oper_priority(item) < oper_priority(oper_stack[-1]):
                if ')' is not item:
                    while oper_stack:
                        value = oper_stack.pop()
                        postfix_stack.append(value)
                    oper_stack.append(item)

                if ')' is item:
                    while oper_stack:
                        value = oper_stack.pop()
                        if '(' is value:
                            break
                        postfix_stack.append(value)

            elif oper_priority(item) == oper_priority(oper_stack[-1]):
                postfix_stack.append(oper_stack.pop())
                oper_stack.append(item)

    if '*' in oper_stack or '/' in oper_stack:
        while oper_stack:
            value = oper_stack.pop()
            postfix_stack.append(value)

    elif '+' in oper_stack or '-' in oper_stack:
        while oper_stack:
            value = oper_stack.pop()
            postfix_stack.append(value)

    print(oper_stack)
    print(postfix_stack)
    return postfix_stack


def oper_priority(opr):
    obj = {
        '*': 4,
        '/': 4,
        '+': 3,
        '-': 3,
        '(': 0,
        ')': 0,
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
        # '((4+2)/4) - (3+2/(7*5))',
        # '3+2/(7*5)',
        # '(1+2*3)/4',
        # '(1*2+3)/4',
        '9-5-5*2-2*9',
        # '1*2+3',
        # '1+2*3',
        # '1+1 + 1',
        # '3-1 + 7',
        # '3+1 - 7',
        # '4- 1',
        # '5 +1',
        # '5 * 2-1',
        # '8/ 2 +2',
    ]
    for e in example:
        result = calculator(e)
        print('calculation result : {} = {}({})'.format(e, int(result), result))
