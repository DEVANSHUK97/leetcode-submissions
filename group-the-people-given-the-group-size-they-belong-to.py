class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        n = len(groupSizes)
        ans_dict = {}
        for i in range(n):
            g_size = groupSizes[i]
            ans_dict[g_size] = ans_dict.get(g_size, []) + [i]
        ans = []
        print(ans_dict)
        for i in ans_dict.keys():
            members = ans_dict[i]
            n_members = len(members)
            j = 0
            while j < n_members:
                ans.append(members[j:j+i])
                j = j + i
        return ans
