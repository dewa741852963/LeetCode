class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = []
        se = list(set(arr))
        for i in range(len(se)):
            count.append(arr.count(se[i]))
        se_count = set(count)
        if len(se_count) == len(count):
            return True
        elif len(se_count) != len(count):
            return False
