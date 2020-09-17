'''
第 0001 题： 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
使用 Python 如何生成 200 个激活码（或者优惠券）？
'''
from random import randint


class N位激活码生成器():
    def __init__(self,想要多少个激活码啊 = 50,多少位 = 4):
        self.size = 想要多少个激活码啊
        self.length = 多少位

    def __iter__(self):
        for i in range(self.size):
            yield self.random_number()

    def random_number(self):
        count = 0
        self.word = ''
        while count < self.length:
            num = randint(48,122)
            if 91 > num >64 or num <58 or num >96:
                self.word += chr(num)
                count += 1
        return self.word
    def __str__(self):
        return 'This can generate {} activation codes with {} digitals.'.format(self.size,self.length)

激活码 = N位激活码生成器(4, 4)


print (激活码)

for i in 激活码:
    print (i)