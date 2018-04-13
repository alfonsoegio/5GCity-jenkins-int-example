#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Rest API """

from configparser import ConfigParser
import random
import logging
import unittest
import threading
import os
import time
import requests

from flask import Flask, Blueprint
from lask_restful import Api
from api.hello import Hello as HelloApi

CONFIG = ConfigParser()
CONFIG.read('conf/config.cfg')
HOST = CONFIG.get('flask', 'host')
PREFIX = CONFIG.get('flask', 'prefix')
API_VERSION = CONFIG.get('flask', 'version')
PORT = int(CONFIG.get('flask', 'port'))
API_BP = Blueprint('api', __name__)
API = Api(API_BP)

URL_PREFIX = '/{prefix}/{version}'.format(
    prefix=PREFIX,
    version=API_VERSION)

APP = Flask(__name__)

LOG = logging.getLogger('werkzeug')
LOG.setLevel(logging.ERROR)

API.add_resource(HelloApi, '/hello', '/hello/<user_name>')

APP.register_blueprint(
    API_BP,
    url_prefix=URL_PREFIX)


class HelloTestCase(unittest.TestCase):
    """ Tests class """

    def test_01(self):
        """ Test Greeting """
        ntests = 10
        time.sleep(3)
        while True:
            user_name = random.choice(['Alice', 'Bob'])
            url = 'http://{0}:{1}/api/v0.1/hello/{2}'.format(HOST,
                                                             PORT,
                                                             user_name)
            response = requests.get(url,
                                    headers={'Content-Type':
                                             'application/json'})
            print(response.text)
            LOG.info(response.text)
            ntests = ntests-1
            if ntests < 0:
                break


if __name__ == "__main__":

    def flask_thread():
        """
        Thread for the API to run the tests against, needed in order
        to execute the random movement tests on main thread
        """
        APP.run(debug=False, host=HOST, port=PORT, threaded=True)

    LOG_THREAD = threading.Thread(target=flask_thread)
    LOG_THREAD.start()
    unittest.main(exit=False)
    os._exit(0)
