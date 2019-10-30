import requests
import re

data = {
    'name': 'ZhangSan',
    'age': 18
}

"""
# 发起请求
r = requests.get('http://httpbin.org/get', data)

print(type(r.text))
print(r.json())
# 解析成字典
print(type(r.json()))
"""

# headers 信息
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# # 请求抓取知乎
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# # 查找匹配字符串
# titles = re.findall(pattern, r.text)
# # 打印匹配的字符串
# print(titles)


# TODO  抓取二进制数据
# # github 头像
# g = requests.get("https://www.ruoduan.cn/music/玫瑰.mp3")
# print(g.text)
# print(g.content)
#
# with open('玫瑰.mp3', 'wb') as f:
#     f.write(g.content)


# # 抓取知乎携带 headers
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# zh = requests.get("https://www.zhihu.com/explore", headers=headers)
# print(zh.text)


# TODO POST 请求

# data = {'name': 'germey', 'age': '22'}
# r = requests.post("http://httpbin.org/post", data=data)
# print(r.text)

# r = requests.get('http://www.ruoduan.com')
# # 用状态码 来判断 请求状态
# exit() if not r.status_code == requests.codes.ok else print('Request Successfully')


# TODO 文件上传
# files = {'file': open('toyxiang.ico', 'rb')}
# f = requests.post('http://httpbin.org/post', files=files)
# print(f.text)

# TODO cookis
# k = requests.get('https://www.baidu.com')
# print(k.cookies)
# for key, val in k.cookies.items():
#     print('%s = %s' % (key, val))

# headers = {
#     'Cookie': '_zap=e3f5e2bd-788d-4143-acfb-fbf8ca581d8a; _xsrf=uP5dnO9vBVC7SNAQP2sbOC8MYrFqHtqo; d_c0="AHCnDOaxHBCPTrsp2Lp_7OfoxWzdXgknOW0=|1569583590"; tst=r; q_c1=6f7f8d2e132648bb9033f5c89e971e9e|1569653221000|1569653221000; tgw_l7_route=64ba0a179156dda09fec37a3b2d556ed; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1571419177,1571420592,1571420948,1572425740; capsion_ticket="2|1:0|10:1572425740|14:capsion_ticket|44:NTdjZDZiMzJiZDdkNGVlNTk3YWRjMWRmZDMxZDRiN2M=|0a9217e4dd619260107aaff5690a59a59c9d109c17c2f2999c0d9b0865ebd63f"; z_c0="2|1:0|10:1572425768|4:z_c0|92:Mi4xUHc1YkF3QUFBQUFBY0tjTTVyRWNFQ2NBQUFDRUFsVk5LTjNnWFFBRzBEeGdqcG05dzRBWTZZc0xHOFRyTlFIYkln|3c1fcf8ac909c375b779c8f57df4f7e643504996158e17c0929ce0f542592140"; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1572425809',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
# }
# r = requests.get('https://www.zhihu.com', headers=headers)
# print(r.text)
#
# with open('tt.txt', 'r+') as f:
#     f.write(r.text)

# TODO 会话维持
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
