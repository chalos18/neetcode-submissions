class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        count_sorted = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))

        count_l = list(count_sorted.items())[0:k]

        top_k = [x[0] for x in count_l]
        
        return top_k
