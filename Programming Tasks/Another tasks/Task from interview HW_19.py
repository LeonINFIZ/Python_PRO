def find_deepest_lake_reliable(heights):
    if len(heights) < 3:
        raise Exception("Not enough heights")

    n = len(heights)

    max_left = [0] * n
    max_left[0] = heights[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], heights[i])

    max_right = [0] * n
    max_right[n - 1] = heights[n - 1]
    for i in range(n - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], heights[i])

    max_depth = 0

    for i in range(n):
        water_level = min(max_left[i], max_right[i])

        depth = water_level - heights[i]

        if depth > max_depth:
            max_depth = depth


    return max_depth


# heights = [3, 3]  ->  ERROR: Not enough heights

heights = [1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 8, 8, 2]

try:
    result = find_deepest_lake_reliable(heights)

    print(f"Heights: {heights}")
    print(f"Max depth of lakes: {result}")
except Exception as e:
    print(f"ERROR: {e}")

