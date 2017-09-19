import urllib.request
import urllib.parse
import re
while (True):
    MyKey = input()
    url = "https://baike.baidu.com/item/" + MyKey
    url = urllib.parse.quote(url)
    url = re.sub("%3A", ':', url)#
    print(url)
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 ''(KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36')

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    pattern = re.compile(r'<div+.+>+.+</div>')
    # pattern = re.compile(r'<div class="para" label-module="para">\s+(.*)\s+</div>')
    result = re.findall(pattern, html)
    # print(result)
    # for each in result:#
    # 	if '<div class="para" label-module="para">' in each:
    # 		new_each = re.sub('<div class="para" label-module="para">', '\n', each)
    #         print(new_each)
    #     elif '' in each:

    '''
    for each in result:
        if '<div class="para" label-module="para">' in each:
            new_each = re.sub('<div class="para" label-module="para">', '\n', each)
            print(new_each)
        else:
            print(each)

    for each in result:
        if '<div class="para" label-module="para">' in each:
            new_each = re.sub('<div class="para" label-module="para">', '\n', each)
            print(new_each)
        else:
            print(each)
    '''

    for each in result:
        new_each = each
        if '<div class="para" label-module="para">' in each:
            new_each = re.sub('<div class="para" label-module="para">', '', each)
            # print(new_each)
            if '<b>' in new_each:
                new_each = re.sub('<b>', '', new_each)
            if '</b>' in new_each:
                new_each = re.sub('</b>', '', new_each)
            if '</div>' in new_each:
                new_each = re.sub('</div>', '', new_each)
                if '<a' in new_each:
                    new_each = re.sub(r'(<[aA][^>]+>[^<]+</[aA]>)', '', new_each)
                print(new_each)
        '''
        if '<div>' in new_each:
            new_each = re.sub('<div>', '', new_each)
        if '<a' in new_each:
            new_each=re.sub(r'(<[aA][^>]+>[^<]+</[aA]>|<[iI][mM][gG][^>]+>)','',new_each)
        if '</a>' in new_each:
            new_each=re.sub('</a>','',new_each)
        print(new_each)#
        '''

