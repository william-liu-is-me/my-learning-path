#分析html

import requests

import re

def get_html(url, code = 'utf - 8'):
    try:
        r = requests.get(url,headers = {'user-agent':'Chrome/10'}) #本网站屏蔽了爬虫软件，需要改headers才能访问
        r.raise_for_status
        r.encoding  = code
        return (r.text)
    except:
        return '出错'



def re_analysis(html,new_list):
    try:
        re_name = r'(?<=<span class="title">)[\w：！·\(\)\s，。.]*(?=</span>)'
        re_rank = r'(?<=ass="">)\d*(?=</em>)'
        re_actor = r'(?<=导演:).*(?=/?..)'
        re_score = r'(?<=average">).*(?=</span>)'
        
        rank_result = re.findall(re_rank,html)
        name_result = re.findall(re_name,html)
        score_result = re.findall(re_score,html)
        actor_result = re.findall(re_actor,html)

    except:
        print('分析出错')
    for i in range(25):
        try:
            new_list.append([rank_result[i],name_result[i],score_result[i],actor_result[i]])
        except:
            continue


def main(num):
    count = 0
    for i in range (num):
        url = f'https://movie.douban.com/top250?start={i*25}&filter='  
        html = get_html(url,code = 'utf - 8')
        new_list = []
        re_analysis(html,new_list)
        for _ in range(25):
            u = new_list[_]
            with open ('movie_list.txt', 'a',encoding = 'utf-8') as f:
                f.write(str(u)+'\n')
        count += 1
        percent = count / num*100
        print ('已完成进度：%.2f'%percent,'%')
            


main(5)


