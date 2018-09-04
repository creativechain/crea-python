from dpay.amount import Amount


def test_amount_init():
    a = Amount('1 BEX')
    assert dict(a) == {'amount': 1.0, 'asset': 'BEX'}
