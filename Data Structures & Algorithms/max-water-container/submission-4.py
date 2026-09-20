class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        largest=0
        for i in range(len(heights)-1):
            # print(f"left-> {heights[left]} right-> {heights[right]}")
            h=min(heights[left],heights[right])
            # print(f"h{h}")
            width = right - left
            # print(f"{right} - {left} = {width}")
            area=h*width
            # print(f"area{area}")
            largest=max(largest,area)
            # print(f"largest{largest}")
            if heights[left]>heights[right]:
                right-=1
            elif heights[left]<heights[right]:
                left+=1
            else:
                left+=1
                right-=1
        return largest