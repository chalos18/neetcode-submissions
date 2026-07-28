class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        intermediate = []
        filtered = []

        for i in range(len(strs)):
            sub_list = [strs[i]]
            for j in range(len(strs)):
                if i != j:
                    filt_i, filt_j = sorted(strs[i]), sorted(strs[j])
                    if filt_i == filt_j:
                        sub_list.append(strs[j])
            sub_list.sort()
            intermediate.append(sub_list)
        
        for sublist in intermediate:
            if sublist not in filtered:
                filtered.append(sublist)

        return filtered

                
