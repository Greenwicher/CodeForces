class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def combinations(work, left, n):
            if n == 0:
                global comb
                comb.append(work)
            else:
                for i in range(len(left)):
                    foo = left[i]
                    if len(work) + len(left) - i + 1 < n:
                        break
                    if not work or foo > work[-1]:
                        tmp = [bar for bar in left if bar != foo]
                        combinations(work + [foo], tmp, n - 1)
            return
        comb = []
        global comb
        nums = sorted(nums)
        for n in range(len(nums) + 1):
            combinations([], nums, n)
        return comb

# Version 2
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        res = [[]]
        for item in nums:
            res += [x + [item] for x in res]
        return res

# Version 3
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        n = len(S)
        S = sorted(S)
        result = []
        for i in range(1<<n):
            temp = []
            for j in range(n):
                if i & (1<<j) > 0:
                    temp.append(S[j])
            result.append(temp)
        return result
