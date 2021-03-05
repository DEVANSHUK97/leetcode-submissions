def helper(map,src):
    q = deque()
    q.append(src)
    n = len(map)
    done = set()
    while len(q):
        element = q.popleft()
        if element not in done:
            done.add(element)
            for i in range(n):
                if map[element][i] == 1 and i not in done:
                    q.append(i)
    print(done)
    return done

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        n = len(isConnected)
        done = set()
        for i in range(n):
            if i not in done:
                all_connected = helper(isConnected, i)
                done.update(all_connected)
                ans = ans + 1
        return ans
