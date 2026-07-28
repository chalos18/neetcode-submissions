class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        count_sorted = sorted(count.items(), key=lambda x: x[1], reverse=True)

        top_k = [x[0] for x in count_sorted[:k]]
        
        return top_k
