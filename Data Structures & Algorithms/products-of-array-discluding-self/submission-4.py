class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        pre = 1
        post = 1

        for i in range(len(nums)):
            if i == 0:
                result[i] = 1
            else:
                result[i] = pre * nums[i-1]
                pre = result[i]

        post = nums[len(nums) - 1]
        print(post)
        print(result)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                pass
            else:
                result[i] = result[i] * post
                post = post * nums[i]

        print(result)

        return result
