import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = re.sub(r'[^a-zA-Z0-9]', '', s)
        a=a.lower()
        i=0
        j=(len(a)-1)
        print(j)
        flag=0
        if len(a)<=1:
            return True
        while j>i:
            print(a[i])
            print(a[j])
            if a[i] == a[j]:
                flag=1
                j-=1
                i+=1
            else:
                flag=0
                break
        if flag==1:
            return True
        else:
            return False