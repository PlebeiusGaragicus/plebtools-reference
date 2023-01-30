"""TODO:
"""

import logging

from pywebio import output

from src.api.authproxy import AuthServiceProxy, JSONRPCException
from src.settings import AppSettings

def return_AuthProxy(settings: AppSettings = None) -> AuthServiceProxy:
    """
        The idea is that we don't have to load the settings file every time we want to connect to the node.
        ... we just store the app settings in a global variable and pass it to this function.
    """
    if settings is None:
        settings = AppSettings()

    user = settings['RPC_USER']
    pswd = settings['RPC_PASS']
    host = settings['RPC_HOST']
    port = settings['RPC_PORT']

    rpc_url = f"http://{user}:{pswd}@{host}:{port}"
    logging.debug("rpc_url=%s", rpc_url)

    return AuthServiceProxy(rpc_url)


def verify_node() -> int | None:
    """
        This will load the settings file and attempt to connect to the node.
        It will return the current block height if successful, or None if not.
    """
    rpc_connection = return_AuthProxy()

    try:
        info = rpc_connection.getblockchaininfo()
        output.toast(f"Node connected - working on {info['chain']} chain")

        tip = rpc_connection.getblockcount()
        return tip
    except JSONRPCException as exception:
        logging.error("Error connecting to node: %s", exception)
        # output.toast("ERROR: Cannot connect to node!", color='error', duration=4)

        output.put_markdown("# Uh oh - cannot connect to node!")
        output.put_text("I can't connect to a bitcoin node.  Make sure the node is running.  Also double check your that bitcoind RPC credentials are correct in settings...")
        output.put_link(name='Open settings', url="./settings")
        output.put_text("") # this is a hack to get a newline between these links
        output.put_link(name='Return to home', url='./')

        return None
