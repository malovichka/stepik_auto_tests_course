def test_abs1_2():
    assert abs(-42) == 42, 'Should be absolute value of a number'

def test_abs2_2():
    assert abs(-42) == -42, 'Should be absolute value of a number'


if __name__ == '__main__':
    test_abs1_2()
    test_abs2_2()