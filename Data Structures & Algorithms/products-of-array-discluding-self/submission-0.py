class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = nums.count(0)

        for i in nums:
            if i != 0:
                total *= i

        answer = []

        for i in nums:
            if zero_count > 1:
                answer.append(0)

            elif zero_count == 1:
                if i == 0:
                    answer.append(total)
                else:
                    answer.append(0)

            else:
                answer.append(total // i)

        return answer