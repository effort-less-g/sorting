class binarySearch:
    def binary_search(nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + (high - low)//2

            if nums[mid] == target:
                return f"Element found at index {mid}"
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return f"Element not found"

llist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

target = 2

result = binarySearch.binary_search(llist, target)

print(result)
