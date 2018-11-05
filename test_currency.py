from currency import convert


def test_convert_same_currency():
    assert convert([], 1, current='USD', to='USD') == 1
    assert convert([], 2, current='USD', to='USD') == 2
