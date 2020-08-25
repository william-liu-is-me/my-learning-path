# Implement strStr() python

'''this is my code'''

haystack = "heslsslloll"
needle = "ba"
if needle in haystack:
    for i in range(len(haystack)-len(needle)+1):
        if haystack[i:i+len(needle)] == needle:
            print (i)
else:
    print('-1')


'''this is the code from Google search, this is way too complicated'''

class Solution(object):
   def strStr(self, haystack, needle):
      """
      :type haystack: str
      :type needle: str
      :rtype: int
      """
      i = 0
      j = 0
      m = len(needle)
      n = len(haystack)
      if m ==0:
         return 0
      while i<n and n-i+1>=m:
         if haystack[i] == needle[j]:
            temp = i
            while j<m and i<n and needle[j]==haystack[i]:
               i+=1
               j+=1
            if j == m:
               return temp
            i= temp+1
            j = 0
         else:
            i+=1
      return -1
haystack = "helloworld"
needle = "lo"
ob1 = Solution()
print(ob1.strStr(haystack, needle))