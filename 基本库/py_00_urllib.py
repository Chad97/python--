import socket
import urllib.request
import urllib.error

# try:
#     response = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('请求超时')


"""
构造 headers
"""
# class urllib.request.Request(url, data=None, headers={}, origin_req_host=None, unverifiable=False, method=None)
#
# from urllib import request, parse
#
# url = 'http://httpbin.org/post'
# headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }
# dict = {'name': 'Germey'}
# data = bytes(parse.urlencode(dict), encoding='utf8')
# req = request.Request(url=url, data=data, headers=headers, method='POST')
# response = request.urlopen(req)
#
# print(response.read().decode('utf-8'))

"""
of
req = request.Request(url=url, data=data, method='POST')  
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
"""

