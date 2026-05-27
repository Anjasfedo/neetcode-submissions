class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        arr = [0] * 26

        for s in strs:
            arr_copy = arr.copy()

            for c in s:
                arr_copy[ord(c) - ord("a")] += 1

            key = " ".join(str(x) for x in arr_copy)

            if key in hash_map:
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]
        
        return list(hash_map.values())