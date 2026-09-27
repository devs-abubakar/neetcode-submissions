class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_list = list(s)
        s_list.sort()
        t_list = list(t)
        t_list.sort()
        for num in range(0,len(s_list)):
            if s_list[num] != t_list[num]:
                return False
        return True
