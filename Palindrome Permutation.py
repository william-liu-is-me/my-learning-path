# question 44:Palindrome Permutation
strs='aabdcdbaa'
start = 0
end = len(strs)-1

while True:
    if strs[start] != strs[end]:
        print ('this is NOT palindrome')
        break
    else:
        start += 1 
        end -= 1
        if end <= start:
            print ('this is palindrome')
            break