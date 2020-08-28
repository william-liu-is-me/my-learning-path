#Best Time to Buy and Sell Stock
'''
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

import copy
stock = [7,6,4,5,3]
copy_of_stock = copy.copy(stock)
copy_of_stock.sort(reverse=True)

if stock==copy_of_stock:
    print('dont buy')
'''only one situation that dont buy: when the stock is decline all the way,
and it will be the same as if you sort the list by reverse sequence. thats why i
use sort(reverse= True) 
'''
else:
    strategy = []
    for i in range(len(stock)):
        for j in range(i+1,len(stock)):
            strategy.append([-stock[i]+stock[j],i,j])

final = max(strategy)
print(f'you can make ${final[0]}，you need to buy it at day {final[1]+1}，sell it at day {final[2]+1}.')