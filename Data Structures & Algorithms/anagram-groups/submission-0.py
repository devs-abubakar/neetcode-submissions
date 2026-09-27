class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        seen = {}
        result = []

        for elem in strs:
            word = "".join(sorted(elem))
            if word not in seen :
                seen[word] = [elem]
            else:
                seen[word].append(elem)
        for items in seen:
            result.append(seen[items])
        return result

                    
                