from example.step02 import calculator


def test_multiple_operator():
    case1 = calculator('1+1 + 1')
    case2 = calculator('3-1 + 7')
    case3 = calculator('3+1- 7')
    case4 = calculator('5 *2  + 1')
    case5 = calculator('5 *2 /2 ')

    assert case1 == 3
    assert case2 == 9
    assert case3 == -3
    assert case4 == 11
    assert case5 == 5
