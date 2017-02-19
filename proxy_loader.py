# -*- coding: utf-8 -*-

import requests
import config
from lxml import etree
import io
import codecs

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
        pass

    def load_online(self):
        r = requests.post(config.url, headers=config.headers, params=config.querystring)
        if r.status_code == requests.codes.ok:
            return r.text
        else:
            r.raise_for_status()

    def parse_loaded(self, data_for_parse):
        parser = etree.HTMLParser(encoding='utf-8')
        tree = etree.parse(io.StringIO(data_for_parse), parser)

        result_data = []

        counter = tree.xpath('count(//*[@id="tblproxy"]/tr)')
        try:
            counter = int(counter)
        except Exception as e:
            raise e

        for item in range(3, counter, 1):
            row = tree.xpath('//*[@id="tblproxy"]/tr[' + str(item) + ']/td/script')

            ip = row[0].text.replace("document.write('", "")
            ip = ip.replace("')", "")
            port = row[1].text.replace("document.write(gp.dep('", "")
            port = port.replace("'))", "")
            port = int(port, 16)

            result_data.append([ip, port])

        return result_data

    def load(self):
        # loaded_data = self.load_online()

        loaded_data = codecs.open("out.html", "r", "utf-8").read()
        parsed_data = self.parse_loaded(loaded_data)
        return parsed_data
