def maxArea(height):
    l, r = 0, len(height) - 1
    ans = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        ans = max(ans, area)
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return ans



height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))


#
#   Max(Area) = Max(diff(index)* min(height))
#   1   8   6   2   5   4   8   3   7
#           i               j       

## min(8, 7) * 7  = 49


# Assume that x <= y
# left: x
# right: y
# Area = min(x,y) * (y - x) = x * (y - x) = x * t
# Area < x * (y - x)
# Left move x (right pointer) and it points to y1 
# -> difference will be y1 - x = t1
# t1 < t && min (x, y1) <= min(x, y)
# if y1 <= y -> min(x, y1) <= min(x,y)
# if y1 > y -> min(x, y1) = x = min (x, y)
# min (x, y1) * t1 < min (x, y) * t
