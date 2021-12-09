#
# @lc app=leetcode.cn id=748 lang=python3
#
# [748] 最短补全词
#

# @lc code=start
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        l=[]
        for i in licensePlate:
            if i.isalpha():
                l.append(i.lower())
        #print(l)
        words.sort(key=len)
        for i in words:
            x=1
            for j in l:
                if (j not in i) or (l.count(j)>i.count(j)):
                    x=0
                    break
            
            if(x==1):
                return(i)
# @lc code=end

