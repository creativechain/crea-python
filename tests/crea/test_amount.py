from crea.amount import Amount


def test_amount_init():
    a = Amount('1 CREA')
    assert dict(a) == {'amount': 1.0, 'asset': 'CREA'}
