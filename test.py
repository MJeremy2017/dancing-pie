"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

l, r => m
"""


def find_target(nums, target):
    l, r = 0, len(nums) - 1
    ans = -1
    while l <= r:
        m = (l + r) >> 1
        if target == nums[m]:
            ans = m
            break
        if nums[r] > nums[m]:
            if nums[m] < target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
        else:
            if nums[m] > target >= nums[l]:
                r = m - 1
            else:
                l = m + 1
    return ans


if __name__ == '__main__':
    testcases = [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1)
    ]

    for a, tgt, want in testcases:
        got = find_target(a, tgt)
        print(got, want)
        assert got == want
