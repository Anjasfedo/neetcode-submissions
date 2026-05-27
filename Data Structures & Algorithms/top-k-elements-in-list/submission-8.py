class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        hash_map = {}

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        print(hash_map)

        pq = []

        for key, val in hash_map.items():
            heapq.heappush(pq, (val, key))

            if len(pq) > k:
                heapq.heappop(pq)

        print(pq)
        return [key for val, key in pq]