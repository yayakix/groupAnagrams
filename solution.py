class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for x in range(len(strs)):
            sortedWord = ''.join(sorted(strs[x]))
            if sortedWord in dict:
                dict[sortedWord].append(strs[x])
            else:
                dict[sortedWord] = [strs[x]]
        return dict.values()
