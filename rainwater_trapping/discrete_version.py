def trap_water(heights):
    n = len(heights)
    if n == 0:
        return 0

    left = [0] * n
    right = [0] * n
    water = 0

    left[0] = heights[0]
    for i in range(1, n):
        left[i] = max(left[i-1], heights[i])

    right[n-1] = heights[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i+1], heights[i])

    for i in range(n):
        water += min(left[i], right[i]) - heights[i]

    return water

print(trap_water([2, 1, 3, 0, 1, 2, 3]))  # Output: 7
