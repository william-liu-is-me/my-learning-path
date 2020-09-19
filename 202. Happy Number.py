#202. Happy Number

#method 1
count = 0

def InitialNumber(num):
    total = 0
    global count
    if count >20: #if by 20 times calculation, 1 is still not reached, break the calc.
        print('calculation over 20 times, stop')
        return 
    for i in str(num):
        total += int(i)**2
    count +=1
    if total ==1:
        print ('calculation:',count,'time(s)')
    else:
        InitialNumber(total)
'''
=========================================
'''

InitialNumber(3)
#not working below
#for i in range(10):
#    InitialNumber(i) 

'''the problem above is that the return will break the recursion,
which is unable to just skip that number

================================================================='''

#method 2 coroutine
'''this is able to skip unhappy number with a limited calculation time.
'''
print ('*'*75)
def subgenerator():
    
    total =0
    while True:
        x = yield
        if x is None:
            break
        total += x**2
    return total

def grouper():
    global key
    while True:
        key = yield from subgenerator()


def main(num):
    count = 0
    original_num = num
    #print (original_num)
    while True:
        count +=1
        if count > 10:
            print(original_num,'calculation over 10 times，stop')
            break
        lst = [int(i) for i in str(num)]
        gen = grouper()
        next(gen)
        for i in lst:
            gen.send(i)
        gen.send(None)
        if key == 1:
            print (original_num,'is happy number，there are :',count,'calculations')
            break
        num = key

for i in range(1,10):
    main(i)