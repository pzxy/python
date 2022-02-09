# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
# 数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3

# 特殊情况： 数组中的最大值小于等于数组的长度的话，可以用这种方法。


def find_repeat_number(nums) -> int:
    i = 0
    l = len(nums)
    while i <= l:
        if i == nums[i]:
            i += 1
            continue
        if nums[i] == nums[nums[i]]:
            return nums[i]
        tmp = nums[i]
        nums[i], nums[tmp] = nums[tmp], nums[i]


d = find_repeat_number([2, 3, 1, 0, 2, 5, 3])
print(d)

i = 0
nums = [2, 3, 1, 0, 2, 5, 3]
nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
print(nums)
