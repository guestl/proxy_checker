# -*- coding: utf-8 -*-

import requests
import config

import logging

# These two lines enable debugging at httplib level (requests->urllib3->http.client)
# You will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
# The only thing missing will be the response.body which is not logged.
try:
    import http.client as http_client
except ImportError:
    # Python 2
    import httplib as http_client
http_client.HTTPConnection.debuglevel = 1

# You must initialize logging, otherwise you'll not see debug output.
logging.basicConfig()
logging.getLogger().setLevel(logging.ERROR)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.ERROR)
requests_log.propagate = True


class Proxy_loader():
    def __init__(self):
        self.headers = {
            'user-agent': config.user_agent,
            'content-type': "application/x-www-form-urlencoded",
            'cache-control': "no-cache",
        }

    def load_online(self, ports):
        self.form_data = config.payload
        r = requests.post(config.proxy_list_url, data=self.form_data, headers=self.headers)
        if r.status_code == requests.codes.ok:
            return r.text
        else:
            r.raise_for_status()

    def parse_loaded(self, data_for_parse):
        return data_for_parse

    def load(self, ports):
        loaded_data = self.load_online(ports)
        parsed_data = self.parse_loaded(loaded_data)
        return parsed_data
