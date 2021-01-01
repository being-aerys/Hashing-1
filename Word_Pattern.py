# Created by Aashish Adhikari at 10:04 AM 12/31/2020

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        hm = {}

        words = s.split()

        if len(pattern) != len(words):
            return False

        # Traverse pattern
        for idx in range(len(pattern)):

            if pattern[idx] not in hm:


                hm[pattern[idx]] = words[idx]
            else:

                if words[idx] != hm[pattern[idx]]:
                    return False

        # Traverse words
        hm = {}
        words = s.split()
        for idx in range(0, len(words)):

            if words[idx] not in hm:


                hm[words[idx]] = pattern[idx]
            else:

                if pattern[idx] != hm[words[idx]] :
                    return False


        return True


