def lengthOfLongestSubstring(s: str) -> int:
        count_map = {}
        n = len(s)
        start = 0
        end = 0
        ans = 0
        while end < n:
            if start == end:
                count_map[s[start]] = 1
                ans = max(ans, end - start + 1)
                # print(f"start is same as end {start} ans is {ans}")
            else:
                count_map[s[end]] = count_map.get(s[end], 0) + 1
                # print(f'count of {s[end]} is {count_map[s[end]]}')
                if count_map[s[end]] > 1:
                    while count_map[s[end]] > 1:
                        # print(f'getting rid of duplication...')
                        count_map[s[start]] = count_map[s[start]] - 1
                        start = start + 1
                        # print(f'left out {s[start]} \n \
                        #       s[start] is now {s[start]} and\n\
                        #       now count_map[s[end]] is {count_map[s[end]]}')
                if ans < end - start + 1:
                    ans = end - start + 1
                    # print(f'new ans is {ans}')
            end += 1
        return ans
    
if __name__ == '__main__':
    print(lengthOfLongestSubstring('pewwkw'))