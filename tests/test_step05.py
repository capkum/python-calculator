from example.step05 import calculator


def test_parentheses():
    example = [
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

    rt = [
        ('20451*+', 65.0),
        ('422+4/322725*/+-', -21.00556),
        ('3275*/+', 3.05714),
        ('42+4/', 1.5),
        ('123*+4/', 1.75),
        ('12*3+4/', 1.25),
        ('905-52*-209*-', -105.0),
        ('512*1-', 101.0),
        ('822/2+', 43),
    ]

    for idx, e in enumerate(example):
        result, postfix = calculator(e)
        assert round(result, 5) == rt[idx][1]
        assert postfix == rt[idx][0]
