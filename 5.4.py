import requests

# kw={'q':'python dict'}

# r=requests.get('http://cn.bing.com/search',params=kw)

# print(r.text)

# https://www.so.com/s?ie=utf-8&fr=none&src=360sou_newhome&q=%E8%BE%BE%E5%BA%B7%E4%B9%A6%E8%AE%B0

ks={'q':'达康书记'}

s=requests.get('https://www.so.com/s',params=ks)

print(s.text)