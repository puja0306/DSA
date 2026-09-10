class Solution:
    def twoSum(self, nums, target):

        arr= [(num,i) for i, num in enumerate(nums)]
        arr.sort()

        left, right= 0, len(arr)-1

        while left< right:
            sum_val = arr[left][0]+ arr[right][0]

            if sum_val==target:
                return [arr[left][1], arr[right][1]]
            elif sum_val< target:
                left+=1
            else:
                right-=1
        return []            


        