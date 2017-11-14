import urllib.request
#r=urllib.request.urlopen('www.nju.edu.cn')

#本地数据获取
'''with open('f:\\Workspace\\python\\Project\\Note\\test.txt','w') as f:#open有返回值 asf:就是讲返回值赋给f:
    f.write('hello world')'''
x=open('test.txt')
p1=x.read(5)#从文件中至多读出size个字节数据，返回一个字符串
p2=x.read()#读文件全部，返回字符串

#print(p1)
print(p2)
x.readline()
x.readlines()
x.seek(offset,whence=0)#在文件中移动文件指针，从whence