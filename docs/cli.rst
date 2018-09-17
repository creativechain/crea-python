creacli CLI
~~~~~~~~~~~
`creacli` is a convenient CLI utility that enables you to manage your wallet, transfer funds, check
balances and more.

Using the Wallet
----------------
`creacli` lets you leverage your BIP38 encrypted wallet to perform various actions on your accounts.

The first time you use `creacli`, you will be prompted to enter a password. This password will be used to encrypt
the `creacli` wallet, which contains your private keys.

You can change the password via `changewalletpassphrase` command.

::

    creacli changewalletpassphrase


From this point on, every time an action requires your private keys, you will be prompted to enter
this password (from CLI as well as while using `crea` library).

To bypass password entry, you can set an environmnet variable ``UNLOCK``.

::

    UNLOCK=mysecretpassword creacli transfer 100 CREA <recipient>

Common Commands
---------------
First, you may like to import your Crea account:

::

    creacli importaccount


You can also import individual private keys:

::

   creacli addkey <private_key>

Listing accounts:

::

   creacli listaccounts

Show balances:

::

   creacli balance account_name1 account_name2

Sending funds:

::

   creacli transfer --account <account_name> 100 CREA <recipient_name> memo

Upvoting a post:

::

   creacli upvote --account <account_name> https://dsite.io/funny/@jared/test-post


Setting Defaults
----------------
For a more convenient use of ``creacli`` as well as the ``crea`` library, you can set some defaults.
This is especially useful if you have a single Crea account.

::

   creacli set default_account jared
   creacli set default_vote_weight 100

   creacli config
    +---------------------+--------+
    | Key                 | Value  |
    +---------------------+--------+
    | default_account     | jared  |
    | default_vote_weight | 100    |
    +---------------------+--------+

If you've set up your `default_account`, you can now send funds by omitting this field:

::

    creacli transfer 100 CREA <recipient_name> memo


Help
----
You can see all available commands with ``creacli -h``

::

    ~ % creacli -h
    usage: creacli [-h] [--node NODE] [--no-broadcast] [--no-wallet] [--unsigned]
                   [--expires EXPIRES] [--verbose VERBOSE] [--version]
                   {set,config,info,changewalletpassphrase,addkey,delkey,getkey,listkeys,listaccounts,upvote,downvote,transfer,powerup,powerdown,powerdownroute,convert,balance,interest,permissions,allow,disallow,newaccount,importaccount,updatememokey,approvewitness,disapprovewitness,sign,broadcast,orderbook,buy,sell,cancel,repost,follow,unfollow,setprofile,delprofile,witnessupdate,witnesscreate}
                   ...

    Command line tool to interact with the Crea network

    positional arguments:
      {set,config,info,changewalletpassphrase,addkey,delkey,getkey,listkeys,listaccounts,upvote,downvote,transfer,powerup,powerdown,powerdownroute,convert,balance,interest,permissions,allow,disallow,newaccount,importaccount,updatememokey,approvewitness,disapprovewitness,sign,broadcast,orderbook,buy,sell,cancel,repost,follow,unfollow,setprofile,delprofile,witnessupdate,witnesscreate}
                            sub-command help
        set                 Set configuration
        config              Show local configuration
        info                Show basic Crea blockchain info
        changewalletpassphrase
                            Change wallet password
        addkey              Add a new key to the wallet
        delkey              Delete keys from the wallet
        getkey              Dump the privatekey of a pubkey from the wallet
        listkeys            List available keys in your wallet
        listaccounts        List available accounts in your wallet
        upvote              Upvote a post
        downvote            Downvote a post
        transfer            Transfer CREA
        powerup             Power up (vest CREA as CREA POWER)
        powerdown           Power down (start withdrawing CREA from CREA POWER)
        powerdownroute      Setup a powerdown route
        convert             Convert CREA Dollars to CREA (takes a week to settle)
        balance             Show the balance of one more more accounts
        interest            Get information about interest payment
        permissions         Show permissions of an account
        allow               Allow an account/key to interact with your account
        disallow            Remove allowance an account/key to interact with your
                            account
        newaccount          Create a new account
        importaccount       Import an account using a passphrase
        updatememokey       Update an account's memo key
        approvewitness      Approve a witnesses
        disapprovewitness   Disapprove a witnesses
        sign                Sign a provided transaction with available and
                            required keys
        broadcast           broadcast a signed transaction
        orderbook           Obtain orderbook of the internal market
        buy                 Buy CREA or CBD from the internal market
        sell                Sell CREA or CBD from the internal market
        cancel              Cancel order in the internal market
        repost             Repost an existing post
        follow              Follow another account
        unfollow            unfollow another account
        setprofile          Set a variable in an account's profile
        delprofile          Set a variable in an account's profile
        witnessupdate       Change witness properties
        witnesscreate       Create a witness

    optional arguments:
      -h, --help            show this help message and exit
      --node NODE           URL for public Crea API (default:
                            "https://cread.creativechain.net")
      --no-broadcast, -d    Do not broadcast anything
      --no-wallet, -p       Do not load the wallet
      --unsigned, -x        Do not try to sign the transaction
      --expires EXPIRES, -e EXPIRES
                            Expiration time in seconds (defaults to 30)
      --verbose VERBOSE, -v VERBOSE
                            Verbosity
      --version             show program's version number and exit
