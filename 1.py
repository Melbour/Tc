import urllib.request
import urllib.parse
import re
urlArray = []#存已经找的网址
def findURL(urlname):
    global urlArray
    if urlname in urlArray:#判断是否这个网页是否在数组中，如果在，代表已经找过，直接返回
        return
    print(urlname)
    urlArray.append(urlname)
    req = urllib.request.Request(urlname)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ''(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    urls = re.findall(r"http://[^\"\'\n;><)]+",html,re.I)


    for i in urls:#遍历找到的所有的网址
         print(i)#输出网址
         #findURL(i)#
    return

urlName="http://www.baidu.com/"

findURL(urlName)
print("已经找完了！\n")