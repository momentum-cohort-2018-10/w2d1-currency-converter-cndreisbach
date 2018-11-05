from currency import convert


def test_convert_same_currency():
    assert convert([], 1, current='USD', to='USD') == 1
    assert convert([], 2, current='USD', to='USD') == 2


def test_convert_usd_to_euros():
    assert convert(
        rates=[("USD", "EUR", 0.74)], value=1, current='USD', to='EUR') == 0.74
