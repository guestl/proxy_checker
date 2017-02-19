# these sites we will use to check if proxy works
check_url = ('lenta.ru', 'cnn.com', 'bbc.co.uk', 'medium.com')

proxy_ports = '8080, 80'

proxy_list_file_name = 'proxies.conf'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

url = "http://www.gatherproxy.com/proxylist/anonymity/"

querystring = {"Type": "elite"}

headers = {'content-type': "application/x-www-form-urlencoded",
           'cache-control': "no-cache",
           'user_agent': user_agent}
