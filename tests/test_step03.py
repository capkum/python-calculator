from example.step03 import calculator


def test_postfix():
    example = [
        '9-5-5*2-2*9',
        '1*2+3',
        '1+2*3',
        '5 +1',
        '5 * 2-1',
        '8/ 2 +2',
    ]
    rt = [-24, 5, 7, 6, 9, 6]

    for idx, e in enumerate(example):
        result = calculator(e)

        assert int(result) == rt[idx]
