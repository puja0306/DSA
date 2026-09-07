class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        # Step 1: Find the majority candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Step 2: Verify candidate (needed if majority element is not guaranteed)
        if nums.count(candidate) > len(nums) // 2:
            return candidate

        return -1  # Return -1 if no majority element exists
