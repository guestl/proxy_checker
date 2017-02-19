# -*- coding: utf-8 -*-

import config
from proxy_checker import Proxy_checker


pc = Proxy_checker()

for site in config.check_url:
    print("\n", site)
