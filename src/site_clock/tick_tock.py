"""TODO:
"""

import json
import time
import logging

from src.api.authproxy import JSONRPCException
from src.node import return_AuthProxy

SLEEP_TIME = 10.0



def respond_to_client():
    """TODO:
    """

    rpc_connection = return_AuthProxy()

    try:
        tip = rpc_connection.getblockcount()
    except JSONRPCException as exc:
        logging.error("Error connecting to node: %s", exc)
        _data = json.dumps({"error":exc.message})
        yield f"id: 1\ndata: {_data}\nevent: message\n\n"
        return

    while True:

        _data = json.dumps({"height":tip})
        yield f"id: 1\ndata: {_data}\nevent: online\n\n"

        time.sleep( SLEEP_TIME )
        tip = rpc_connection.getblockcount()
