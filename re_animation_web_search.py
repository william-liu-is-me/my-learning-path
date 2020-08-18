import requests
import re


def get_html(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def parse_page(ulist,html):
    try:
        name_pattern = re.findall(r'alt=\".*?\"',html)
        desc_pattern = re.findall(r'(?<=<p>).*(?=<)',html)
        
        for i in range(min(len(name_pattern),(len(desc_pattern)))):
            name = name_pattern[i].split('"')[1]
            desc = desc_pattern[i]
            ulist.append([name,desc])
    except:
        print('')


def print_list(ulist):
    tplt = '{:3}\t{:20}\t{:1000}'
    print (tplt.format('序号','漫画名','描述'))
    count = 0
    for g in ulist:
        count += 1
        print (tplt.format(count,g[0],g[1]))
    



def main():
    dong_man_ming = str(input('type of animation you want to search：'))
    depth = 2
    ulist =[]
    
    for i in range(depth):
        try:
            url = f'http://www.yhdm.tv/search/{dong_man_ming}/?page={i+1}'
            html = get_html(url)
            parse_page(ulist,html)
        except:
            print('main出错')
    print_list(ulist)

main()
