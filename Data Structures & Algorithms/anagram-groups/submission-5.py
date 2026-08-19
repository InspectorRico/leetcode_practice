class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #what're the constraints
        #all lowercase letters
        #group the anagrams together
        # add them to the list

        anagram_list = defaultdict(list)

        for s in strs:
            anagram_builder = {}
            for c in s:
                if c in anagram_builder:
                    anagram_builder[c] += 1
                else:
                    anagram_builder[c] = 1

            anagram_list[tuple(sorted(anagram_builder.items()))].append(s)

        return list(anagram_list.values())