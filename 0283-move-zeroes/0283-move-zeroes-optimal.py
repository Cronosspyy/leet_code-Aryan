class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        lst = []

        for i in range(0, n):
            if nums[i] != 0:
                lst.append(nums[i])
        nz = len(lst)
        for i in range(0,nz):
            nums[i] = lst[i]
        for i in range(nz,n):
            nums[i] = 0