#3. Longest Substring Without Repeating Characters
'''
Given a string s, find the length of the longest substring without 
repeating characters.
'''
#word = "abcabcbb"
#word ="bbbbb"
word = "pwwkew"


def fn2(word):
    my_dict = dict()
    for i in range(len(word)):
        sample = word[i]
        for j in range(i+1,len(word)):
            if word[j] in sample:
                my_dict[str(sample)]=len(sample)
                break
            sample += word[j]
            if j == len(word)-1:
                my_dict[str(sample)]=len(sample)
    
    longest_value = max([v for v in my_dict.values()])
    for k,v in my_dict.items():
        if v == longest_value:
            print (k)

#fn2(word)


#5. Longest Palindromic Substring
word = "babad"

def find_palind(word):
    my_str = ''
    lst = []
    for _ in word:
        lst.append(_)
    for q in range(len(lst)):
        if lst[q] != lst[(-q)-1]:
            break
        my_str += lst[q]
    return my_str


def look_up(word):
    for i in range(len(word)-1,0,-1):
        for j in range(0,len(word)-i):
            test_word = word[j:(i+1+j)]
            result = find_palind(test_word)
            if result:
                print (result) 
