def find_value(nums: list[int] | range, value: int) -> bool:
    """
    hhihihi
    """
    low = 0
    high = len(nums) - 1
    result = False
    while low <= high:
           
        mid = (low + high) // 2
        guess = nums[mid]

        if guess == value:
            result = True
            return result
        if guess > value:
            high = mid - 1
        else:
            low = mid + 1

    return result   



     

