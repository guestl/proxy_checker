# these sites we will use to check if proxy works
check_url = ('lenta.ru', 'cnn.com', 'bbc.co.uk', 'medium.com')

proxy_list_url = 'http://proxylist.hidemyass.com/'
proxy_ports = '8080, 80'

proxy_list_file_name = 'proxies.conf'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

payload = 'a%5B%5D=1&a%5B%5D=2&a%5B%5D=3&ac=on&allPorts=0&' \
          'c%5B%5D=China&c%5B%5D=Venezuela&c%5B%5D=Indonesia&c%5B%5D='\
          'United+States&c%5B%5D=Brazil&c%5B%5D=Russian+Federation&'\
          'c%5B%5D=Ukraine&c%5B%5D=Bulgaria&c%5B%5D=Bangladesh&c%5B%5D=Italy&'\
          'c%5B%5D=United+Kingdom&c%5B%5D=Thailand&c%5B%5D=Hong+Kong&c%5B%5D=Egypt&'\
          'c%5B%5D=Czech+Republic&c%5B%5D=Korea%2C+Republic+of&c%5B%5D=Australia&c%5B%5D='\
          'Taiwan&c%5B%5D=Chile&c%5B%5D=Nepal&c%5B%5D=Taiwan&c%5B%5D=Ghana&c%5B%5D=Bolivia&'\
          'c%5B%5D=Sierra+Leone&c%5B%5D=Paraguay&c%5B%5D=Viet+Nam&c%5B%5D=Costa+Rica&'\
          'c%5B%5D=Azerbaijan&c%5B%5D=South+Africa&c%5B%5D=Netherlands&c%5B%5D=Armenia&'\
          'c%5B%5D=Ecuador&c%5B%5D=Belgium&c%5B%5D=Germany&c%5B%5D=India&c%5B%5D=France&'\
          'c%5B%5D=Hungary&c%5B%5D=Poland&c%5B%5D=United+Arab+Emirates&c%5B%5D=Japan&'\
          'c%5B%5D=Canada&c%5B%5D=Slovakia&c%5B%5D=Peru&c%5B%5D=Spain&c%5B%5D=Argentina&'\
          'ct%5B%5D=2&ct%5B%5D=3&o=0&p=80%2C8080&pl=off&pp=3&pr%5B%5D=0&pr%5B%5D=1&pr%5B%5D=2&'\
          's=0&sortBy=date&sp%5B%5D=2&sp%5B%5D=3'

# form params without ports
# payload = "id=proxy-search-form&ac=on&allPorts=0&p=8080%2C80&pr%5B%5D=&pr%5B%5D=2&a%5B%5D=&a%5B%5D=4&pl=on&sp%5B%5D=2&sp%5B%5D=3&ct%5B%5D=2&ct%5B%5D=3&s=0&o=0&pp=3&sortBy=Date"
