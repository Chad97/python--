import requests
from requests.auth import HTTPBasicAuth
from requests import Request, Session

# proxies = {'https': 'http://user:password@10.10.1.10:3128/',}
# requests.get('https://www.taobao.com', proxies=proxies)
#
#
# # TODO socks 代理
# # pip3 install"requests[socks]"
# proxies = {
#     'http': 'socks5://user:password@host:port',
#     'https': 'socks5://user:password@host:port'
# }
# requests.get('https://www.taobao.com', proxies=proxies)

# TODO 超时设置

# r = requests.get('https://www.taobao.com', timeout=1)
# print(r.status_code)


# TODO 身份认证
# r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username', 'password'))
# print(r.status_code)

# TODO OAuth1 认证
# from requests_oauthlib import OAuth1
#
# url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
# auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
#               'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
# requests.get(url, auth=auth)


# TODO Prepared Request

url = 'http://httpbin.org/post'
data = {'name': 'germey'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}

s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
