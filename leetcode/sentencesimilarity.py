class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        for a, b in zip(words1, words2):
            if [a, b] not in pairs and [b, a] not in pairs and a != b:
                return False

        return True
