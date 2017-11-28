from example import step01


def test_step01_singl_operator():

        rt = step01.calculator('1 + 1')
        assert rt == 2
        rt = step01.calculator('4- 1')
        assert rt == 3
        rt = step01.calculator('5* 2')
        assert rt == 10
        rt = step01.calculator('5/2')
        assert rt == 2.5
