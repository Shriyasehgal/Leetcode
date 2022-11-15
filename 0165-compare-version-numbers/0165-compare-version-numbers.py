class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')
        for a, b in zip_longest(version1,version2,fillvalue = '0'):
            a = int(a)
            b = int(b)
            if a > b: return 1
            if a < b: return -1
        return 0
        