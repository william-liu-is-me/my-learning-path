#第 0004 题： 任一个英文的纯文本文件，统计其中的单词出现的个数。

from time import time

start = time()

file_name = 'fulldemo.txt'#the file must be within the same dir, or you need to tell
#python the location of the file.
with open(file_name,encoding ='utf-8') as file_obj:
    file_content = ''
    size = 100
    while True:
        content = file_obj.read(size)
        if not content:
            break
        file_content += content
#读取文件


import re

RE_WORDS = re.compile(r'\w+')

words = RE_WORDS.findall(file_content)

#把文章内容整理出来，每个单词都放在列表里面，去掉了空格和标点符号
#print (words)
from collections import Counter
result = Counter(words)
def results():
    for k,v in sorted(result.items(),key = lambda x:x[1],reverse=True):
        if 100 > v > 50:
            print (f'{k} ---> {v} times.') 
results()
end = time()

print (end -start)
#把结果打出来