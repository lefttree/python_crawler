import urllib2
enable_proxy = False

proxy_server = {'http': 'http://some-proxy.com:8080'}
proxy_handler = urllib2.ProxyHandler(proxy_server)
null_proxy_handler = urllib2.ProxyHandler({})

if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)


#timeout setup, 3rd parameter in urlopen
response = urllib2.urlopen("http://www.google.com", timeout=10)
print response.read()
#response = urllib2.urlopen("http://www.google.com", data, 10)
