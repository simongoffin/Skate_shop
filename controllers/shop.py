# -*- coding: utf-8 -*-

from openerp import http
from openerp.addons.web.controllers import main

class shop(main.Home):


    @app.route('/service_plus', methods=["POST"])
    def service_plus():
        data = flask.request.json
        a = data["a"]
        b = data["b"]
        delay = data.get("delay", 0)
        time.sleep(delay)
        return flask.jsonify(**{
            "addition": a + b,
        })

    @app.route('/service_mult', methods=["POST"])
    def service_mult():
        data = flask.request.json
        a = data["a"]
        b = data["b"]
        delay = data.get("delay", 0)
        time.sleep(delay)
        return flask.jsonify(**{
            "multiplication": a * b,
        })