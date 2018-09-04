from dpay.dpayd import DPayd
from dpay.commit import Commit
from dpaybase.exceptions import RPCError


def test_transfer():
    wif = '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3'
    c = Commit(dpayd_instance=DPayd(nodes=[]),
               keys=[wif])

    rpc_error = None
    try:
        c.transfer('test2', '1.000', 'BEX', 'foo', 'test')
    except RPCError as e:
        rpc_error = str(e)
    else:
        raise Exception('expected RPCError')

    assert 'tx_missing_active_auth' in rpc_error


def test_claim_reward():
    wif = '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3'
    c = Commit(dpayd_instance=DPayd(nodes=[]),
               keys=[wif])

    rpc_error = None
    try:
        c.claim_reward_balance(
            account='test',
            reward_dpay='1.000 BEX',
            reward_vests='0.000000 VESTS',
            reward_bbd='0.000 BBD')
    except RPCError as e:
        rpc_error = str(e)
    else:
        raise Exception('expected RPCError')

    assert 'tx_missing_posting_auth' in rpc_error


def test_witness_update():
    # TODO: Remove when witness_update is fixed.
    return
    wif = '5KQwrPbwdL6PhXujxW37FSSQZ1JiwsST4cqQzDeyXtP79zkvFD3'
    c = Commit(dpayd_instance=DPayd(nodes=[]),
               keys=[wif])

    signing_key = 'DWB1111111111111111111111111111111114T1Anm'
    props = {
        'account_creation_fee': '0.500 BEX',
        'maximum_block_size': 65536,
        'bbd_interest_rate': 0}

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
