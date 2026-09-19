class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count the frequency of each number
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Step 2: Bucket array where index = frequency
        # Maximum frequency possible is len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        # Step 3: Iterate from highest frequency to lowest
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result