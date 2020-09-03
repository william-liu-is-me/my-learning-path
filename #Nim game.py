#小测试
from random import randint

total_stones = 8
flag = True
print (f'现在有苹果{total_stones}个')
while True:
    if total_stones == 0:
        if flag == True:
            print('玩家胜利')
        else:
            print('电脑胜利')
        break
    else:
        while True:
            n = int(input('玩家拿走数量：'))
            if 1<= n and n <= 3:
                break
            else:
                print('请重新输入1到3的数字')
    total_stones -= n
    flag = True
    print(f'现在还剩下{total_stones}个')
    if total_stones == 0:
        if flag == True:
            print('玩家胜利')
        else:
            print('电脑胜利')
        break
    if total_stones % 4 != 0:
        n = total_stones % 4
        total_stones -= n
        print(f'电脑拿走了{n}个，还剩下{total_stones}个')
        flag = False
        
    else:
        n = randint(1,3)
        total_stones -= n
        print(f'电脑拿走了{n}个，还剩下{total_stones}个')
        flag = False
            
        

input()