from .commit import Commit
from .cread import Cread


class Crea:
    """ Connect to the Crea network.

        Args:

            nodes (list): A list of Crea HTTP RPC nodes to connect to. If
            not provided, official Crea nodes will be used.

            debug (bool): Elevate logging level to `logging.DEBUG`.
            Defaults to `logging.INFO`.

            no_broadcast (bool): If set to ``True``, committal actions like
            sending funds will have no effect (simulation only).

        Optional Arguments (kwargs):

        Args:

            keys (list): A list of wif keys. If provided, the Wallet will
            use these keys rather than the ones found in BIP38 encrypted
            wallet.

            unsigned (bool): (Defaults to False) Use this for offline signing.

            expiration (int): (Defualts to 60) Size of window in seconds
            that the transaction needs to be broadcasted in, before it
            expires.

        Returns:

            Cread class instance. It can be used to execute commands
            against Crea node.

        Example:

           If you would like to override the official Crea nodes
           (default), you can pass your own.  When currently used node goes
           offline, ``Cread`` will automatically fail-over to the next
           available node.

           .. code-block:: python

               nodes = [
                   'https://cread.yournode1.com',
                   'https://cread.yournode2.com',
               ]

               s = Cread(nodes)

       """

    def __init__(self, nodes=None, no_broadcast=False, **kwargs):
        self.cread = Cread(nodes=nodes, **kwargs)
        self.commit = Commit(
            cread_instance=self.cread, no_broadcast=no_broadcast, **kwargs)

    def __getattr__(self, item):
        """ Bind .commit, .cread methods here as a convenience. """
        if hasattr(self.cread, item):
            return getattr(self.cread, item)
        if hasattr(self.commit, item):
            return getattr(self.commit, item)
        if item.endswith("_api"):
            return Crea.Api(api_name=item, exec_method=self.cread.call)

        raise AttributeError('Crea has no attribute "%s"' % item)

    class Api(object):
        def __init__(self, api_name="", exec_method=None):
            self.api_name = api_name
            self.exec_method = exec_method
            return

        def __getattr__(self, method_name):
            return Crea.Method(
                api_name=self.api_name,
                method_name=method_name,
                exec_method=self.exec_method,
            )

    class Method(object):
        def __init__(self, api_name="", method_name="", exec_method=None):
            self.api_name = api_name
            self.method_name = method_name
            self.exec_method = exec_method
            return

        def __call__(self, *args, **kwargs):
            assert not (args and kwargs), "specified both args and kwargs"
            if len(kwargs) > 0:
                return self.exec_method(
                    self.method_name, kwargs=kwargs, api=self.api_name)
            return self.exec_method(self.method_name, *args, api=self.api_name)


if __name__ == '__main__':
    s = Crea()
    print(s.get_account_count())