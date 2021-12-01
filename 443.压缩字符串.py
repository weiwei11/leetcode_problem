#
# @lc app=leetcode.cn id=443 lang=python3
#
# [443] 压缩字符串
#

# @lc code=start
class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0: return 0
        count = 0
        p = -1
        flag = False
        for i in range(0, len(chars)):
            # if not flag:
            #     p += 1
            #     count += 1
            #     chars[p] = chars[i]
            #     flag = True
            if p >= 0 and chars[p] == chars[i]:
                count += 1
            else:
                p += 1
                if count > 1:
                    s = str(count)
                    for j in range(len(s)):
                        chars[p + j] = s[j] 
                    p = p + len(s)
                count = 1
                chars[p] = chars[i]
                print(chars[p], p, chars[i], i)
            
            # print(chars)
            # print(p, count)
        p += 1
        if count > 1:
            s = str(count)
            for i in range(len(s)):
                chars[p + i] = s[i] 
            p = p + len(s)
        
        return p

# @lc code=end

