class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l < r:
            if s [l] != s[r]:
                skipl,skipr = s[l+1:r+1],s[l:r]
                return (skipl== skipl[::-1] or skipr == skipr[::-1])
            r-=1
            l+=1
        return True

    
        