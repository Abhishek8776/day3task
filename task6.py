arr = [0, 1, 3, 8, 14, 18, 19, 34, 52]
target = 17
left = 0
right = len(arr) - 1
while left <= right:
    mid = (left + right) // 2   
    if arr[mid] == target:
        print(f"Found {target} at index {mid}")
        break
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(f"{target} not found in the list")
