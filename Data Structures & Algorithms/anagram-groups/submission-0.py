class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for s in strs:
            key = list(s)
            letters = key.sort()
            hashmap[tuple(key)].append(s)

        return list(hashmap.values())            

            
            