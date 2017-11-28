from example.step04 import calculator


def test_parentheses():
    example = [
        '((4+2)/4) - (3+2/(7*5))',
        '3+2/(7*5)',
        '(4+2)/4',
        '(1+2*3)/4',
        '(1*2+3)/4',
        '9-5-5*2-2*9',
        '5 * 2-1',
        '8/ 2 +2',
    ]

    rt = [
        ('42+4/3275*/+-', -1.55714),
        ('3275*/+', 3.05714),
        ('42+4/', 1.5),
        ('123*+4/', 1.75),
        ('12*3+4/', 1.25),
        ('95-52*-29*-', -24.0),
        ('52*1-', 9.0),
        ('82/2+', 6.0),
    ]

    for idx, e in enumerate(example):
        result, postfix = calculator(e)
        assert round(result, 5) == rt[idx][1]
        assert postfix == rt[idx][0]
