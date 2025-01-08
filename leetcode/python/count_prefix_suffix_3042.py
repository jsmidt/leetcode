# Author Joseph Smidt

def isPrefixAndSuffix(str1, str2) -> bool:
    n = len(str1)
    return str1 == str2[:n] and str1 == str2[-n:]

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        tot = 0
        lenn = len(words)
        for i in range(lenn):
            tot += sum([isPrefixAndSuffix(words[i], words[j]) for j in range(i+1,lenn)])
        return (tot)
