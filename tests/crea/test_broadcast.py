from crea.cread import Cread
from crea.commit import Commit
from creabase.exceptions import RPCError


def test_transfer():
    wif = '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3'
    c = Commit(cread_instance=Cread(nodes=[]),
               keys=[wif])

    rpc_error = None
    try:
        c.transfer('test2', '1.000', 'CREA', 'foo', 'test')
    except RPCError as e:
        rpc_error = str(e)
    else:
        raise Exception('expected RPCError')

    assert 'tx_missing_active_auth' in rpc_error


def test_claim_reward():
    wif = '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3'
    c = Commit(cread_instance=Cread(nodes=[]),
               keys=[wif])

    rpc_error = None
    try:
        c.claim_reward_balance(
            account='test',
            reward_crea='1.000 CREA',
            reward_vests='0.000000 VESTS',
            reward_cbd='0.000 CBD')
    except RPCError as e:
        rpc_error = str(e)
    else:
        raise Exception('expected RPCError')

    assert 'tx_missing_posting_auth' in rpc_error


def test_witness_update():
    # TODO: Remove when witness_update is fixed.
    return
    wif = '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3'
    c = Commit(cread_instance=Cread(nodes=[]),
               keys=[wif])

    signing_key = 'CREA1111111111111111111111111111111114T1Anm'
    props = {
        'account_creation_fee': '0.500 CREA',
        'maximum_block_size': 65536,
        'cbd_interest_rate': 0}

    rpc_error = None
    try:
        c.witness_update(
            signing_key=signing_key,
            account='test',
            props=props,
            url='foo')
    except RPCError as e:
        rpc_error = str(e)
    else:
        raise Exception('expected RPCError')

    assert 'tx_missing_active_auth' in rpc_error
