import urllib.request
import requests
'''
<html>
<head>
<title>test</title>
<body>
hhhhhhhhhhh
</body>
</head>
</html>
''''''
访问成功，状态码为200
资源不存在，404'''
#r=urllib.request.urlopen('https://jw.nju.edu.cn')（积极拒绝什么鬼
r=urllib.request.urlopen('https://www.baidu.com')
html=r.read()
#print(html)
r2=requests.get('http://www.baidu.com')
#print(r2.status_code)
r3=requests.request('GET','http://z.cn')
#事实上requests里所有的方法都是来自request一个
#print(r3.status_code)
#print(r3.encoding)
print(r2.text)
print(r2.encoding)#百度用的编码是标准库ISO-8859-1，而不是UTF-8
print(r2.apparent_encoding)#根据body部分解析网页真正使用的编码方式
r2.encoding='utf-8'#指定编码方式
print(r2.text)
#若为二进制串，则用content，而不是text

