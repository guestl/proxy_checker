# -*- coding: utf-8 -*-

import config
from proxy_loader import Proxy_loader
import codecs


class Proxy_checker():
    proxies_list = []

    def __init__(self):
        pl = Proxy_loader()
        self.proxies_list = pl.load(config.proxy_ports)
        file = codecs.open('out.html', 'w', 'utf-8')
        file.writelines(self.proxies_list)
        file.close()

    def check_proxy(self, proxy):
        pass
