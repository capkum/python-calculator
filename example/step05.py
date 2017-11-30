'''
example 변수안의 식만을 계산
목표 두자리수 계산하기~
'''
import re


def calculator(str):
    get_postfix = generator_postfix(str)
    numbers = []

    for item in get_postfix:
        if item.isdigit():
            numbers.append(item)
        else:
            y = float(numbers.pop())
            x = float(numbers.pop())

            numbers.append(formula(item)(x, y))

    return numbers[0], ''.join(get_postfix)


# postfix후위 표기법으로 변환
def generator_postfix(str):
    target = calculator_regx(str)
    postfix_stack = []
    oper_stack = []

    for idx, item in enumerate(target):
        if item.isdigit():
            postfix_stack.append(item)

        else:
            new_item = oper_priority(item)

            if len(oper_stack) == 0:
                oper_stack.append(item)

            elif new_item > oper_priority(oper_stack[-1]):
                if ')' is not item:
                    oper_stack.append(item)

            elif new_item == oper_priority(oper_stack[-1]):
                if '(' in oper_stack:
                    if '(' is item:
                        oper_stack.append(item)
                    else:
                        postfix_stack.append(oper_stack.pop())
                else:
                    while oper_stack:
                        postfix_stack.append(oper_stack.pop())
                    oper_stack.append(item)

            elif new_item < oper_priority(oper_stack[-1]):
                    if ')' is item:
                        while oper_stack:
                            value = oper_stack.pop()
                            if '(' is value:
                                break
                            postfix_stack.append(value)

                    else:
                        if '(' is item:
                            oper_stack.append(item)

                        else:
                            while oper_stack:
                                value = oper_stack.pop()
                                if '(' is value:
                                    oper_stack.append(item)
                                    break

                                else:
                                    postfix_stack.append(value)
                                    if len(oper_stack) is 0:
                                        oper_stack.append(item)
                                        break

    if len(oper_stack) is not 0:
            while oper_stack:
                value = oper_stack.pop()
                postfix_stack.append(value)

    return postfix_stack


# 두자리 연산을 위한 정규식
def calculator_regx(str):
    reg = re.compile(r'(?:(?<=[^\d\.])(?=\d)|(?=[^\d\.]))', re.MULTILINE)
    return [x for x in re.sub(reg, " ", str).split(" ") if x]


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
        '((411+2)/4) - (3+2/(7*5))',
        '3+2/(7*5)',
        '(4+2)/4',
        '(1+2*3)/4',
        '(1*2+3)/4',
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
        '20+45*1',
        '((42+2)/4) - (32+2/(72*5))',
        '3+2/(7*5)',
        '(4+2)/4',
        '(1+2*3)/4',
        '(1*2+3)/4',
        '90-5-5*2-20*9',
        '51 * 2-1',
        '82/ 2 +2',
    ]
    for idx, e in enumerate(example):
        result, postfix = calculator(e)
        int_tp = int(result)
        float_tp = round(result, 5)
        print('{}] postfix => {}'.format(idx, postfix))
        print('calculation result : {} = {}({})\n'.format(e, int_tp, float_tp))
