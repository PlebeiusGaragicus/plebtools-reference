#!/usr/bin/env python3

import sys
import logging
import json
import time

from flask import Flask, render_template, Response
import pywebio

from . import config

# BUILT-IN
from . import tool_settings

# GOOD ENOUGH
from . import tool_rpccurlhelper
from . import tool_currencyconvert
from . import tool_opreturn

# WORKING ON...
from . import tool_miningcalc

# ON HOLD...
# from . import tool_dashboard
# from . import tool_braiinspool
# from . import tool_blockstreamsat
# from . import tool_historicalanalysis
# from . import tool_treasurymanagement
# from . import tool_sideloader
# from . import tool_terminal

from . import site_clock

app = Flask(__name__, static_folder='../web/static', template_folder='../web/templates')


@app.route("/")
def index():
    return render_template("index.html", title=config.APP_TITLE)


@app.route("/clock")
def clock():
    return render_template("clock.html")


@app.route("/listen")
def listen():
    return Response(site_clock.respond_to_client(), mimetype='text/event-stream')

@app.route("/contribute")
def contribute():
    return render_template("contribute.html", title=config.APP_TITLE)


def setup_logging() -> None:

    logging.basicConfig(
        level=logging.DEBUG if config.DEBUG else logging.INFO,
        format="%(name)s [%(levelname)s] (%(filename)s @ %(lineno)d) %(message)s",

        ### TODO CRASHED! PermissionError: [Errno 13] Permission denied: '/debug.log'
        handlers=[logging.FileHandler("./data/debug.log", mode='a'), logging.StreamHandler(sys.stdout)] if config.DEBUG == True else [logging.StreamHandler(sys.stdout)],
    )

    if config.DEBUG is True:
        #logging.getLogger("pywebio").addHandler([logging.StreamHandler(sys.stdout), logging.FileHandler("debug.log", mode='a')])
        logging.getLogger("pywebio").addHandler(logging.StreamHandler(sys.stdout))
    else:
        logging.getLogger("werkzeug").setLevel(logging.WARNING)
        logging.getLogger("pywebio").setLevel(logging.WARNING)

    # don't log the tornado webserver stuff
    logging.getLogger("tornado.access").setLevel(logging.WARNING)

    logging.debug("DEBUG MODE: %s", config.DEBUG)
    logging.debug("arguments: %s", sys.argv)


if __name__ == "__main__":
    setup_logging()

    # BUILT-IN
    app.add_url_rule('/settings', 'settings', pywebio.platform.flask.webio_view( tool_settings.main ), methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods

    # GOOD ENOUGH
    app.add_url_rule('/curl_formatter', 'curl_formatter', pywebio.platform.flask.webio_view( tool_rpccurlhelper.main ), methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods
    app.add_url_rule('/currency_converter', 'currency_converter', pywebio.platform.flask.webio_view( tool_currencyconvert.main ), methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods
    app.add_url_rule('/opreturn', 'opreturn', pywebio.platform.flask.webio_view( tool_opreturn.main ), methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods

    # WORKING ON...
    app.add_url_rule('/mining_calcs', 'mining_calcs', pywebio.platform.flask.webio_view( tool_miningcalc.main ), methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods

    # ON HOLD...
    # app.add_url_rule('/dashboard', 'dashboard', pywebio.platform.flask.webio_view( tool_dashboard.main ), methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods
    # app.add_url_rule('/braiinspool', 'braiinspool', pywebio.platform.flask.webio_view( tool_braiinspool.main ), methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods
    # app.add_url_rule('/blockstreamsat', 'blockstreamsat', pywebio.platform.flask.webio_view( tool_blockstreamsat.main ), methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods
    # app.add_url_rule('/historicalanalysis', 'historicalanalysis', pywebio.platform.flask.webio_view( tool_historicalanalysis.main ), methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods
    # app.add_url_rule('/treasurymanagement', 'treasurymanagement', pywebio.platform.flask.webio_view( tool_treasurymanagement.main ), methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods
    # app.add_url_rule('/sideloader', 'sideloader', pywebio.platform.flask.webio_view( tool_sideloader.main ), methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods
    # app.add_url_rule('/terminal', 'terminal', pywebio.platform.flask.webio_view( tool_terminal.main ), methods=['GET', 'POST', 'OPTIONS'])  # need GET,POST and OPTIONS methods

    app.run(host='0.0.0.0', port=config.PORT, debug=config.DEBUG)
