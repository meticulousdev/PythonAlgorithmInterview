# %%
from typing import List

# %%
class Solution:
    # soln two points
    def trap_tp(self, height: List[int]) -> int:
        if not height:
            return 0

        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume

    # soln stack
    def trap_st(self, height: List[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume

# %%
if __name__ == "__main__":
    nums: list[int] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    
    soln = Solution()
    ret = soln.trap_tp(nums)
    print(ret)

    ret = soln.trap_st(nums)
    print(ret)


